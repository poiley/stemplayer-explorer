import json
import re
import os

class stem_player():
    def __init__(self, device):
        self.device = device
        self.mount_path = os.path.abspath(self.device.name)
        self.config = self.Config(self.mount_path)
        self.library = self.Library(self.mount_path)

    class Config():
        def __init__(self, root_dir):
            self.filename = "config.txt"
            self.dir = os.path.abspath(root_dir)
            self.file = open('{}\{}'.format(self.dir, self.filename), 'r')
            self.file_contents = self.file.read()
            self.json = json.loads(self.file_contents)

    class Library():
        def __init__(self, root_dir):
            self.dir = os.path.abspath(root_dir)
            self.album_folders = self.get_album_folders()
            self.albums = self.parse_album_folders()
            
        def get_album_folders(self):
            return [f for f in os.listdir(self.dir) if re.match('A[0-9]', f)]      

        def parse_album_folders(self):
            albums = []
            for album_folder in self.get_album_folders():
                albums.append(Album('{}\{}'.format(self.dir, album_folder)))
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

class Album():
    def __init__(self, dir):
        self.name = dir.split('\\')[2]
        self.filename = "ALBUM.TXT"
        self.dir = os.path.abspath(dir)
        self.metadata_file = open('{}\{}'.format(self.dir, self.filename), 'r')
        self.metadata_file_contents = self.metadata_file.read()
        self.metadata = json.loads(self.metadata_file_contents)
        self.tracks = self.get_tracks()

    def get_tracks(self):
        tracks = []
        for track_dir in [ f for f in os.listdir(self.dir) if self.filename not in f]:
            tracks.append(Track('{}\{}'.format(self.dir, track_dir)))
        return tracks

    def __str__(self):
        return '[A] {} - {}'.format(self.name, self.metadata['title'])

class Track():
    def __init__(self, dir):
        self.filename = 'TRACK.TXT'
        self.dir = os.path.abspath(dir)
      
        self.metadata_file = open('{}\{}'.format(self.dir, self.filename), 'r')
        self.metadata_file_contents = str(self.metadata_file.read())

        if self.metadata_file_contents[-1] != '}':
            self.metadata_file_contents = self.metadata_file_contents[:-1]

        self.metadata = json.loads(self.metadata_file_contents)
        self.stems = self.get_stems()
    
    def get_stems(self):
        return [f for f in os.listdir(self.dir) if self.filename not in f]

    def __str__(self):
        return '[T] {}'.format(self.metadata['metadata']['title'])