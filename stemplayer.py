from asyncore import file_dispatcher
import json
import os

class stem_player():
    def __init__(self, device):
        self.device = device
        self.mount_path = os.path.abspath(self.device.name)
        self.config = self.Config(self.mount_path)

    class Config():
        def __init__(self, config_dir):
            self.filename = "config.txt"
            self.dir = os.path.abspath(config_dir)

            self.file = open('{}\{}'.format(self.dir, self.filename), 'r')
            self.file_contents = self.file.read()
            self.json = json.loads(self.file_contents)
            print(self.file_contents)
            print(self.json)
            

    class Library():
        def __init__(self):
            self.root = ""