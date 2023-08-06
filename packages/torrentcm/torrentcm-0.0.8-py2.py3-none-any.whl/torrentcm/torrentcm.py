import argparse
import io
import math
from pathlib import Path
import qbittorrentapi
import rich
import yaml
from platformdirs import *
from rich.live import Live
from rich.table import Table
import itertools
DEFAULT_CONFIG_PATH = site_config_dir("TorrentClientManager")




# Forked from https://github.com/divijbindlish/parse-torrent-name
# Patch applied at https://github.com/ezggeorge/parse-torrent-name
# MIT LICENCED
import re
patterns = [
    ('season', '(s?([0-9]{1,2}))[ex]'),
    ('episode', '([ex]([0-9]{2})(?:[^0-9]|$))'),
    # Year limit fix by https://github.com/bensen9sticks
    # old  ('year', '([\[\(]?((?:19[0-9]|20[01])[0-9])[\]\)]?)')
    ('year', '([\[\(]?((?:19[0-9]|20[0-9])[0-9])[\]\)]?)'),
    #--------------------
    ('resolution', '([0-9]{3,4}p)'),
    ('quality', ('((?:PPV\.)?[HP]DTV|(?:HD)?CAM|B[DR]Rip|(?:HD-?)?TS|'
                 '(?:PPV )?WEB-?DL(?: DVDRip)?|HDRip|DVDRip|DVDRIP|'
                 'CamRip|W[EB]BRip|BluRay|DvDScr|hdtv|telesync)')),
    ('codec', '(xvid|[hx]\.?26[45])'),
    ('audio', ('(MP3|DD5\.?1|Dual[\- ]Audio|LiNE|DTS|'
               'AAC[.-]LC|AAC(?:\.?2\.0)?|'
               'AC3(?:\.5\.1)?)')),
    ('group', '(- ?([^-]+(?:-={[^-]+-?$)?))$'),
    ('region', 'R[0-9]'),
    ('extended', '(EXTENDED(:?.CUT)?)'),
    ('hardcoded', 'HC'),
    ('proper', 'PROPER'),
    ('repack', 'REPACK'),
    ('container', '(MKV|AVI|MP4)'),
    ('widescreen', 'WS'),
    ('website', '^(\[ ?([^\]]+?) ?\])'),
    ('language', '(rus\.eng|ita\.eng)'),
    ('sbs', '(?:Half-)?SBS'),
    ('unrated', 'UNRATED'),
    ('size', '(\d+(?:\.\d+)?(?:GB|MB))'),
    ('3d', '3D')
]
types = {
    'season': 'integer',
    'episode': 'integer',
    'year': 'integer',
    'extended': 'boolean',
    'hardcoded': 'boolean',
    'proper': 'boolean',
    'repack': 'boolean',
    'widescreen': 'boolean',
    'unrated': 'boolean',
    '3d': 'boolean'
}
class PTN(object):
    def _escape_regex(self, string):
        return re.sub('[\-\[\]{}()*+?.,\\\^$|#\s]', '\\$&', string)

    def __init__(self):
        self.torrent = None
        self.excess_raw = None
        self.group_raw = None
        self.start = None
        self.end = None
        self.title_raw = None
        self.parts = None

    def _part(self, name, match, raw, clean):
        # The main core instructuions
        self.parts[name] = clean

        if len(match) != 0:
            # The instructions for extracting title
            index = self.torrent['name'].find(match[0])
            if index == 0:
                self.start = len(match[0])
            elif self.end is None or index < self.end:
                self.end = index

        if name != 'excess':
            # The instructions for adding excess
            if name == 'group':
                self.group_raw = raw
            if raw is not None:
                self.excess_raw = self.excess_raw.replace(raw, '')

    def _late(self, name, clean):
        if name == 'group':
            self._part(name, [], None, clean)
        elif name == 'episodeName':
            clean = re.sub('[\._]', ' ', clean)
            clean = re.sub('_+$', '', clean)
            self._part(name, [], None, clean.strip())

    def parse(self, name):
        self.parts = {}
        self.torrent = {'name': name}
        self.excess_raw = name
        self.group_raw = ''
        self.start = 0
        self.end = None
        self.title_raw = None

        for key, pattern in patterns:
            if key not in ('season', 'episode', 'website'):
                pattern = r'\b%s\b' % pattern

            clean_name = re.sub('_', ' ', self.torrent['name'])
            match = re.findall(pattern, clean_name, re.I)
            if len(match) == 0:
                continue

            index = {}
            if isinstance(match[0], tuple):
                match = list(match[0])
            if len(match) > 1:
                index['raw'] = 0
                index['clean'] = 1
            else:
                index['raw'] = 0
                index['clean'] = 0

            if key in types.keys() and types[key] == 'boolean':
                clean = True
            else:
                clean = match[index['clean']]
                if key in types.keys() and types[key] == 'integer':
                    clean = int(clean)
            if key == 'group':
                if re.search(patterns[5][1], clean, re.I) \
                        or re.search(patterns[4][1], clean):
                    continue  # Codec and quality.
                if re.match('[^ ]+ [^ ]+ .+', clean):
                    key = 'episodeName'
            if key == 'episode':
                sub_pattern = self._escape_regex(match[index['raw']])
                self.torrent['map'] = re.sub(
                    sub_pattern, '{episode}', self.torrent['name']
                )
            self._part(key, match, match[index['raw']], clean)

        # Start process for title
        raw = self.torrent['name']
        if self.end is not None:
            raw = raw[self.start:self.end].split('(')[0]

        clean = re.sub('^ -', '', raw)
        if clean.find(' ') == -1 and clean.find('.') != -1:
            clean = re.sub('\.', ' ', clean)
        clean = re.sub('_', ' ', clean)
        clean = re.sub('([\[\(_]|- )$', '', clean).strip()

        self._part('title', [], raw, clean)

        # Start process for end
        clean = re.sub('(^[-\. ()]+)|([-\. ]+$)', '', self.excess_raw)
        clean = re.sub('[\(\)\/]', ' ', clean)
        match = re.split('\.\.+| +', clean)
        if len(match) > 0 and isinstance(match[0], tuple):
            match = list(match[0])

        clean = filter(bool, match)
        clean = [item for item in filter(lambda a: a != '-', clean)]
        clean = [item.strip('-') for item in clean]
        if len(clean) != 0:
            group_pattern = clean[-1] + self.group_raw
            if self.torrent['name'].find(group_pattern) == \
                    len(self.torrent['name']) - len(group_pattern):
                self._late('group', clean.pop() + self.group_raw)

            if 'map' in self.torrent.keys() and len(clean) != 0:
                episode_name_pattern = (
                    '{episode}'
                    '' + re.sub('_+$', '', clean[0])
                )
                if self.torrent['map'].find(episode_name_pattern) != -1:
                    self._late('episodeName', clean.pop(0))

        if len(clean) != 0:
            if len(clean) == 1:
                clean = clean[0]
            self._part('excess', [], self.excess_raw, clean)
        return self.parts
# ---







# https://stackoverflow.com/a/14822210
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])



def init_config():
    Path(DEFAULT_CONFIG_PATH).mkdir(parents=True, exist_ok=True)
    config_file = Path(DEFAULT_CONFIG_PATH, 'config.yaml')
    # Check if json config exists, if not create it and exit with info message
    if config_file.is_file():
        with open(config_file,"r") as user_file:
            config_parsed = yaml.safe_load(user_file)
            return config_parsed

    else:
        data = {"tracker_messages": ["Torrent not registered with this tracker."],
                "clients": [{"connect":False ,"type":"qbittorrent","host": "localhost", "port": 8080, "username": "admin", "password": "adminadmin"},
                            {"connect":False ,"type":"qbittorrent","host": "localhost", "port": 8080, "username": "admin", "password": "adminadmin"}
                            ]}
        with io.open(config_file, 'w', encoding='utf8') as outfile:
            yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)
        rich.print(
            f"[bold yellow]Config File not detected, create a template at {config_file}\nEdit this file with your qbittorrent credentials.")
        return False




class QBIT():
    def __init__(self,host,username,password,port,tracker_codes):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.tracker = tracker_codes
        self.client = qbittorrentapi.Client(
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            REQUESTS_ARGS={'timeout': (5, 30)},
        )

    def check_connection(self):
        try:
            self.client.auth_log_in()
            info = {"qbit_version":self.client.app.version,"qbit_webapi_version":self.client.app.web_api_version,"build_info": self.client.app.build_info.items(),"torrents_info":self.client.torrents_info()}
            return info
        except qbittorrentapi.APIError as e:
            rich.print(f"[bold red]{e}")
            return False
    
    def autotag(self,dry_run:bool=False,title:bool=False,audio:bool=False,resolution:bool=False,codec:bool=False,season_number:bool=False,group:bool=False,quality:bool=False):
        
        replacement_items = {
        '!': ' ',
        '-': ' ',
        '.': ' ',
        '[': ' ',
        ']': ' ',
        '(': ' ',
        ')': ' ',
        }

        

        table = Table()
        with Live(table, refresh_per_second=4):
            table.add_column("[bold yellow]Processed")
            table.add_column("[bold yellow]Hash")
            table.add_column("[bold yellow]Name")
            table.add_column("[bold yellow]Tags")
            for torrent in self.client.torrents_info():
                # Sanitize characters
                for key, value in replacement_items.items():
                    if key in torrent.name:
                        torrent.name = torrent.name.replace(key, value)
                # Name parser
                data = PTN().parse(torrent.name)
                try:
                    # From https://stackoverflow.com/a/3159166
                    data['excess'] = [x for x in data['excess'] if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]
                    # ---
                except KeyError:
                    pass
                try:
                    season = re.findall(r'(S\d*)',data['title'])[0]
                    data['title'] = data['title'].replace(season,'').rstrip()
                    if season is not None:
                        data['season'] = season
                except IndexError:
                    pass
                data.pop('year',None)
                data.pop('proper', None)
                data.pop('excess', None)
                if not title:
                    data.pop('title', None)
                if not codec:
                    data.pop('codec', None)
                if not resolution:
                    data.pop('resolution', None)
                if not audio:
                    data.pop('audio', None)
                if not group:
                    data.pop('group', None)
                if not quality:
                    data.pop('quality', None)
                if not season_number:
                    data.pop('season', None)
                
                # Flatten dict to list for qbit
                tags = []
                for key in data:
                    tags.append(data[key])


                if not dry_run:
                    if tags is not None: 
                        self.client.torrent_tags.add_tags(tags=tags, torrent_hashes=torrent.hash)
                        table.add_row("[greed]✓",str(torrent.hash), str(torrent.name),str(tags))
                    else:
                        table.add_row("[greed]✓",str(torrent.hash), str(torrent.name),'None')
                else:
                    if tags is not None: 
                        table.add_row("[red]X",str(torrent.hash), str(torrent.name),str(tags))
                    else:
                        table.add_row("[red]X",str(torrent.hash), str(torrent.name),'None')

                
                


                

            


    def clean_torrents(self,dry_run:bool=False,keep_files:bool=False):

        dead = []
        table = Table()

        with Live(table, refresh_per_second=4):
            table.add_column("[bold yellow]Dead")
            table.add_column("[bold yellow]Hash")
            table.add_column("[bold yellow]Name")
            table.add_column("[bold yellow]Size")
            for torrent in self.client.torrents_info():
                temp = self.client.torrents_trackers(torrent_hash=torrent.hash)
                if temp[3]['msg'] in self.tracker_messages:
                    dead.append(torrent.hash)
                    table.add_row("[green]✓",str(torrent.hash), str(torrent.name),convert_size(torrent.size))
                else:
                    table.add_row("[red]X",str(torrent.hash), str(torrent.name), convert_size(torrent.size))
        if not dead and not dry_run:
            if keep_files:
                rich.print('[bold yellow]Please wait, removing torrents and deleting files....')
                self.client.torrents_delete(delete_files=True, torrent_hashes=dead)
            else:
                rich.print('[bold yellow]Please wait, removing torrents without deleting files....')
                self.client.torrents_delete(delete_files=False, torrent_hashes=dead)
        else:
            rich.print("There is nothing to do...")




def main():
    # Argument Init
    parser = argparse.ArgumentParser(
    prog='Torrent Client Manager',
    description='CLI Tool to help you manage your torrents.',
    epilog='Made with ❤')
    
    parser.add_argument('-dryrun',
                        action='store_true', help='Does not interact with torrents, still contacts clients for status.')
    parser.add_argument('-k', '--keep-files',
                        action='store_true', help='Does not delete files when removing torrents, used with -c or --clean, does nothing on its own.')
    parser.add_argument('-c', '--clean',
                        action='store_true', help='Removes torrents that are not registered with their trackers.')
    parser.add_argument('-autotag',
                        action='store_true', help='Automatically tags your torrents based on filenames.')
    parser.add_argument('-tagtitle',
                    action='store_true', help='Used with -autotag, includes title (Might break)')
    parser.add_argument('-tagaudio',
                    action='store_true', help='Used with -autotag, includes audio codec')
    parser.add_argument('-tagresolution',
                    action='store_true', help='Used with -autotag, includes resolution')
    parser.add_argument('-tagcodec',
                    action='store_true', help='Used with -autotag, includes codec')
    parser.add_argument('-tagseason',
                    action='store_true', help='Used with -autotag, includes season number')
    parser.add_argument('-taggroup',
                    action='store_true', help='Used with -autotag, includes group tags')
    parser.add_argument('-tagquality',
                    action='store_true', help='Used with -autotag, includes quality tags etc. Bluray, DBRip')
    args = parser.parse_args()

    #Check config
    config = init_config()
    if not config:
        rich.print("[bold red]Exiting...")
        exit()
    else:
        for item in config['clients']:
            if item['connect']:
                if item['type'] == 'qbittorrent':
                    qbit = QBIT(host=item['host'],username=item['username'],password=item['password'],port=item['port'],tracker_codes=config['tracker_messages'])
                    rich.print(f"Connecting to [bold blue]{item['host']}...")
                    status = qbit.check_connection()
                    if status == False:
                        rich.print(f"[bold red]Failed to connect to [bold blue]{item['host']}")
                    else:
                        rich.print(f"[bold yellow]Sucess!")
                        rich.print(f"Qbittorrent Version : [bold yellow]{status['qbit_version']}")
                        rich.print(f"Qbittorrent WebAPI Version : [bold yellow]{status['qbit_version']}")
                        rich.print(f"Torrents detected : [bold yellow]{len(status['torrents_info'])}")
                        print('\n')
                        # Check dryrun
                        if args.dryrun == True:
                            string = "[bold green]True"
                        else:
                            string = "[bold red]False"
                        rich.print(f"DRY RUN IS SET TO {string}")
                        if args.clean:
                                qbit.clean_torrents(dry_run=args.dryrun,keep_files=args.k)
                        if args.autotag:
                                qbit.autotag(dry_run=args.dryrun,title=args.tagtitle,audio=args.tagaudio,resolution=args.tagresolution,codec=args.tagcodec,season_number=args.tagseason,group=args.taggroup,quality=args.tagquality)
                    
                elif item['type'] == 'deluge':
                    pass
                elif item['type'] == 'rutorrent':
                    pass
                elif item['type'] == 'rutorrent':
                    pass
                else:
                    rich.print("[bold red]Error parsing client type from config file, please check your config settings.")
                    exit()
            else:
                pass
    



if __name__ == "__main__":
    main()
    