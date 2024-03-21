import os
import shutil
from tkinter import messagebox
import getpass

class Functionality:
    def copyThe_files(self, des_location, copyFile_list):
        for i in copyFile_list:
            shutil.copy(i, des_location)
        messagebox.showinfo("info","copied successfully")

    def moveThe_files(self, des_location, moveFile_list):
        for i in moveFile_list:
            shutil.move(i, des_location)
        messagebox.showinfo('info', "moved successfully")
    
    def delThe_file(self, del_location):
        os.remove(del_location)
        messagebox.showinfo("info", "delete successfully")

    def copyThe_dir(self,current_location, des_location):
        try:
            if os.path.exists(des_location):
                temp_dest = os.path.join(des_location, os.path.basename(current_location))

            shutil.copytree(current_location, temp_dest)
            messagebox.showinfo("info", "copied successfully")
        except FileExistsError as f:
            print(f.FileExistsError)
    
    def moveThe_dir(self,current_location, des_location):
        shutil.move(current_location, des_location)
        messagebox.showinfo("info", "Successfully moved")

    def os_name(self):
        self.my_osName = os.name
        if self.my_osName == "posix":
            return "Linux"
        elif self.my_osName == "nt":
            return "Window"

    def user_name(self):
        return getpass.getuser()
    
    def cwd(self):
        return os.getcwd()

