import os
from os.path import exists
from os.path import isfile
from common_module import common_module

class find_from_list(common_module):
    """
    Searches for a list of files in a given directory recursively
    """

    def __init__(self, args):
        super().__init__('Find from list')
        self.file_list = args.file_list
        self.target_dir = args.target_dir

    def list_files(self, filelist):
        if exists(filelist) and isfile(filelist):
            file = open(filelist, 'r')
            return [f.strip() for f in file.readlines()]
        else:
            print(f'file {filelist} does not exist or is not a file')
            return None

    def exec_task(self):
        filelist = self.list_files(self.file_list)
        for root, _, files in os.walk(self.target_dir):
            for file in files:
                if file in filelist:
                    print(f'{root}/{file}')
