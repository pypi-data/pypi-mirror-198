# torrent-client-manager
 Torrent Client Manager is a CLI utility for managing torrent client instances

# Installation

requirements
You need a qbittorrent instance with a WEBGUI interface, currently works with qbittorrent only (tested with versions 4.2.0 and up)

and now you can do
```
pip install torrentcm
```

# Usage
```
torrentcm -h

usage: Torrent Client Manager [-h] [-dryrun] [-k] [-c] [-autotag] [-tagtitle] [-tagaudio] [-tagresolution] [-tagcodec] [-tagseason] [-taggroup] [-tagquality]

CLI Tool to help you manage your torrents.

options:
  -h, --help        show this help message and exit
  -dryrun           Does not interact with torrents, still contacts clients for status and results.
  -c, --clean       Removes torrents that are not registered with their trackers.
  -autotag          Automatically tags your torrents based on filenames.
  -k, --keep-files  Used with --clean / -c ,Does not delete files when removing torrents, used with -c or --clean, does nothing on its own.
  -tagtitle         Used with -autotag, includes title (Might break)
  -tagaudio         Used with -autotag, includes audio codec
  -tagresolution    Used with -autotag, includes resolution
  -tagcodec         Used with -autotag, includes codec
  -tagseason        Used with -autotag, includes season number
  -taggroup         Used with -autotag, includes group tags
  -tagquality       Used with -autotag, includes quality tags etc. Bluray, DBRip

Made with ❤
```
