from shutil import copy2 as copy
from os.path import exists
from os.path import isfile
from common_module import common_module

class copy_from_list(common_module):
    """
    Copy a list of files
    """

    def __init__(self, args):
        super().__init__('Search in file content')
        self.file_list = args.file_list
        self.destination_dir = args.destination_dir
        self.target_dir = args.target

    def list_files(self, filelist):
        if exists(filelist) and isfile(filelist):
            file = open(filelist, 'r')
            return [f.strip() for f in file.readlines()]
        else:
            print(f'file {filelist} does not exist or is not a file')
            return None

    def exec_task(self):
        files_to_copy = self.list_files(self.file_list)
        if files_to_copy:
            print(f'Copying {len(files_to_copy)} files')
            destination_dir = self.destination_dir
            target_dir = self.target_dir
            if exists(destination_dir) and exists(target_dir):
                for file in files_to_copy:
                    print(f'Copying {file} to {destination_dir}')
                    try:
                        copy(file, destination_dir)
                    except Exception as e:
                        print(e)
            else:
                print('Make sure both origin and destionation exists.')
        else:
            print('There are no files to copy')
