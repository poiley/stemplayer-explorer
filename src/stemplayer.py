import json
import re
import os
from mount import os_str 

class stem_player(object):
    def __init__(self, device):
        self.device = device
        self.mount_path = self._parse_path(device)
        self.path_delimiter = '\\' if os_str == 'Windows' else '/'
        self.config = self.Config(self)
        self.library = self.Library(self)

    def _parse_path(self, path):
        if os_str == 'Windows':
            return os.path.abspath(self.device.name)
        elif os_str == 'Linux':
            return os.path.abspath(path)

    def __str__(self):
        if os_str == 'Windows':
            return self.device.VolumeSerialNumber
        elif os_str == 'Linux':
            return self.device[:-12] # /STEM PLAYER is 12 characters

    class Config(object):
        def __init__(self, stem_player):
            self.stem_player = stem_player
            self.filename = "config.txt"
            self.dir = os.path.abspath(self.stem_player.mount_path)
            self.file = open('{}{delim}{}'.format(self.dir, self.filename, delim=self.stem_player.path_delimiter), 'r')
            self.file_contents = self.file.read()
            self.json = json.loads(self.file_contents)

    class Library(object):
        def __init__(self, stem_player):
            self.stem_player = stem_player
            self.dir = os.path.abspath(self.stem_player.mount_path)
            self.album_folders = self.get_album_folders()
            self.albums = self.parse_album_folders()
            
        def get_album_folders(self):
            return [f for f in os.listdir(self.dir) if re.match('A[0-9]', f)]      

        def parse_album_folders(self):
            albums = []
            for album_folder in self.get_album_folders():
                albums.append(Album('{}{delim}{}'.format(self.dir, album_folder, delim=self.stem_player.path_delimiter), self.stem_player.path_delimiter))
            return albums

        def get_album(self, dir):
            for album in self.albums:
                if album.dir == dir:
                    return album
                    
        def __str__(self):
            out = ''
            for album in self.albums:
                out += '{}\n'.format(album)
                for track in album.tracks:
                    out += '  {}\n'.format(track)
            return out[:-1]

class Album(object):
    def __init__(self, dir, delim):
        self.path_delimiter = delim
        self.name = dir.split(self.path_delimiter)[2]
        self.filename = "ALBUM.TXT"
        self.dir = os.path.abspath(dir)
        self.metadata_file = open('{}{delim}{}'.format(self.dir, self.filename, delim=self.path_delimiter), 'r')
        self.metadata_file_contents = self.metadata_file.read()
        self.metadata = json.loads(self.metadata_file_contents)
        self.tracks = self.get_tracks()

    def get_tracks(self):
        tracks = []
        for track_dir in [ f for f in os.listdir(self.dir) if self.filename not in f]:
            tracks.append(Track('{}{delim}{}'.format(self.dir, track_dir, delim=self.path_delimiter), self.path_delimiter))
        return tracks

    def __str__(self):
        return '[A] {} - {}'.format(self.name, self.metadata['title'])

class Track(object):
    def __init__(self, dir, delim):
        self.filename = 'TRACK.TXT'
        self.dir = os.path.abspath(dir)
        self.path_delimiter = delim
        self.metadata_file = open('{}{delim}{}'.format(self.dir, self.filename, delim=self.path_delimiter), 'r')
        self.metadata_file_contents = str(self.metadata_file.read())

        if self.metadata_file_contents[-1] != '}':
            self.metadata_file_contents = self.metadata_file_contents[:-1]

        self.metadata = json.loads(self.metadata_file_contents)
        self.stems = self.get_stems()
    
    def get_stems(self):
        return [f for f in os.listdir(self.dir) if self.filename not in f]

    def __str__(self):
        return '[T] {}'.format(self.metadata['metadata']['title'])