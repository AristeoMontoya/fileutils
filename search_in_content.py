import re
from os.path import exists
from os.path import isfile
from common_module import common_module

class search_in_content(common_module):
    """
    This module searches for a given regex
    in a file or list of files.
    """

    def __init__(self, args):
        super().__init__('Search in file contents')
        self.file_list = args.file_list
        self.regex = f'.*({args.criteria}).*'

    def list_files(self, filelist):
        if exists(filelist) and isfile(filelist):
            file = open(filelist, 'r')
            return [f.strip() for f in file.readlines()]
        else:
            print(f'file {filelist} does not exist or is not a file')
            return None

    def get_file_content(self, filename):
        file = open(filename, 'r')
        return file.read()

    def exec_task(self):
        files = self.list_files(self.file_list)
        if files:
            for file in files:
                print(f'Processing {file}')
                content = self.get_file_content(file)
                match = re.search(self.regex, content)
                if match:
                    print(match.group(0))
                    print()
        else:
            print('There are no files to search in')
