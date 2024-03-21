from fileOrganize import *
import os
import shutil

class Extension_wise:
    def __init__(self,file_path):
        self.main_path = file_path
        self.move_files = FileManager(self.main_path)
        self.move_files.organize_files()

        for folders in os.listdir(self.main_path):
            folder = os.path.join(self.main_path, folders)
            lis_items = os.listdir(folder)

            i = 0
            while i < len(lis_items):
                j = 0
                # print("hi")
                file_path = os.path.join(folder, lis_items[i])
                name, extension = os.path.splitext(lis_items[i])
                extension = extension[1:]
                i = i + 1
                extension_folders = os.path.join(folder, extension)
                if not os.path.exists(extension_folders):
                    os.mkdir(extension_folders)
                if not os.path.isdir(file_path):
                    shutil.move(file_path, extension_folders)   
                j+=1