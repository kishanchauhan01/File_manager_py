from extension_wise import Extension_wise
from functionalities import Functionality
import tkinter as tk
from tkinter import messagebox, filedialog

#fonts
HEAD_LINE = ("Purisa",24,"bold")

#colors
SKY_BLUE = "#87CEEB"
LIGHT_GRAY = "#F5F5F5"
off_WHITE = ("#F8FAFF")

class FileManager_gui:
    functionalities_file = Functionality()
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x500")
        self.window.resizable(0,0)
        self.top_frame = self.create_top_frame()
        self.content_top_frame = self.createLabel_top_frame()
        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack()
        self.options = self.options_btn()
        self.organize = self.organize_btn()
        self.img = self.bottom_img()

    def createLabel_top_frame(self):
        '''
        This method create the content of the top frame and use the parent window as top_frame
        '''
        label = tk.Label(self.top_frame, text="File Manager",bg=SKY_BLUE, height=2, font=HEAD_LINE)
        label.pack(padx=5, pady=5)
        return label

    def create_top_frame(self):
        '''
        This method create the top frame in which we I reflect the content
        '''
        frame = tk.Frame(self.window,bg=SKY_BLUE)
        frame.pack(expand=False, fill='x')
        return frame
    
    def browse_copyMove(self,entery):
        '''
        This method give interface of the browsing only for copy/move the file and it also insert that path into the entery. Here we can select multiple files
        '''
        self.copyMoveFile_list = list(filedialog.askopenfilenames())
        entery.insert('1', self.copyMoveFile_list)

    def browse_dir(self,entery):
        self.copyMove_dir_list = str(filedialog.askdirectory())
        entery.insert('1', self.copyMove_dir_list)
    
    def browse_paste(self, entery):
        '''
        This method give interface for the destination location only for copy/move the file and it also insert 
        the full path of that directory
        '''
        paste_directory = str(filedialog.askdirectory())
        entery.insert('1', paste_directory)

    def copy_the_files(self):
        '''
        This method just call the copy method of the Functionality class and that function copy the files
        '''
        des_location = self.destFile_name.get()
        self.functionalities_file.copyThe_files(des_location, self.copyMoveFile_list)

    def move_the_files(self):
        '''
        This method just call the move method of the Functionality class and that function move the files
        '''
        des_location = self.destFile_name.get()
        self.functionalities_file.moveThe_files(des_location, self.copyMoveFile_list)
    
    def copy_move_file_window(self):
        '''
        This method just create another frame which provides the fuinctionaly of copy/move file
        and if there is any other frame is open then first it close that frame and after that it open this frame
        '''
        try:
            if(self.pop_del_window.winfo_exists()):
                self.pop_del_window.destroy()

        except AttributeError:
            print(AttributeError)
        
        try:
            if(self.pop_cmdir.winfo_exists()):
                self.pop_cmdir.destroy()
                
        except AttributeError:
            print(AttributeError)
        
        finally:
            self.pop_window = tk.Frame(self.options_window,bg="#f5bf69")
            self.pop_window.place(x=0, y=300)
            # global copyFile_name, destFile_name
            self.copyFile_name = tk.StringVar()
            self.destFile_name = tk.StringVar()
            label = tk.Label(self.pop_window, text="Select the file:-)", bg="#f5bf69")
            label.grid(row=1, column=1, padx=5, pady=5)
            label1 = tk.Label(self.pop_window, text="Where to paste:-)", bg="#f5bf69")
            label1.grid(row=2, column=1, padx=5, pady=5)
            entery = tk.Entry(self.pop_window, textvariable=self.copyFile_name, width=50)
            entery.grid(row=1, column=2, padx=5, pady=5)
            entery1 = tk.Entry(self.pop_window, textvariable=self.destFile_name, width=50)
            entery1.grid(row=2, column=2, padx=5, pady=5)
            #browse buttons
            button = tk.Button(self.pop_window, text="Browse", command= lambda: self.browse_copyMove(entery))
            button.grid(row=1, column=3, padx=5,pady=5)
            button1 = tk.Button(self.pop_window, text="Browse", command= lambda: self.browse_paste(entery1))
            button1.grid(row=2, column=3, padx=5,pady=5)
            #copy and move button and exit button
            copy_button = tk.Button(self.pop_window, text="Copy", command=self.copy_the_files)
            copy_button.grid(row=3, column=1, padx=5, pady=5)
            move_button = tk.Button(self.pop_window, text="Move", command=self.move_the_files)
            move_button.grid(row=3, column=2, padx=5, pady=5)
            exit_button = tk.Button(self.pop_window, text="Exit", command=self.pop_window.destroy)
            exit_button.grid(row=3, column=3, padx=5, pady=5)
            self.pop_window.mainloop()

    def browse_del_file(self, entery):
        '''
        This method give the interface for browsing the files only for the deleting the files
        '''
        delFlile_list = list(filedialog.askopenfilenames())
        entery.insert('1', delFlile_list)

    def del_the_file(self):
        '''
        This method delete the files you selct by calling the metod of the class Functionality
        '''
        del_location = self.del_file_name.get()
        self.functionalities_file.delThe_file(del_location)

    def delete_the_file_window(self):
        try:
            if(self.pop_window.winfo_exists()):
                self.pop_window.destroy()

        except AttributeError:
            print(AttributeError)
        
        try:
            if(self.pop_cmdir.winfo_exists()):
                self.pop_cmdir.destroy()
                
        except AttributeError:
            print(AttributeError)

        finally:
            self.pop_del_window = tk.Frame(self.options_window, bg="#f5bf69")
            self.pop_del_window.place(x=0, y=330)
            # global del_file_name
            self.del_file_name = tk.StringVar()
            label = tk.Label(self.pop_del_window, text="Select the file \n you want to delete", bg="#f5bf69")
            label.grid(row=0, column=0, padx=5, pady=5)
            entery = tk.Entry(self.pop_del_window, textvariable=self.del_file_name, width=50)
            entery.grid(row=0, column=1, padx=5, pady=5)
            button = tk.Button(self.pop_del_window, text="Browse", command=lambda: self.browse_del_file(entery), bg="yellow")
            button.grid(row=0, column=2, padx=5, pady=5)
            del_button = tk.Button(self.pop_del_window, text="Delete", command= self.del_the_file)
            del_button.grid(row=1, column=0, padx=5, pady=5)
            exit_window = tk.Button(self.pop_del_window, text="Exit", command=self.pop_del_window.destroy)
            exit_window.grid(row=1, column=1, padx=5, pady=5)
            self.pop_del_window.mainloop()

    def copy_the_dir(self):
        self.functionalities_file.copyThe_dir(self.cm_folder_name.get(), self.cm_destFolder_name.get())
    
    def move_the_dir(self):
        self.functionalities_file.moveThe_dir(self.cm_folder_name.get(), self.cm_destFolder_name.get())

    def copy_moveDir_window(self):
        try:
            if(self.pop_del_window.winfo_exists()):
                self.pop_del_window.destroy()
                

        except AttributeError:
            print(AttributeError)
        
        try:
            if(self.pop_window.winfo_exists()):
                self.pop_window.destroy()
                
        except AttributeError:
            print(AttributeError)

        finally:
            self.pop_cmdir = tk.Frame(self.options_window, bg="#f5bf69")
            self.pop_cmdir.place(x=0, y=300)
            self.cm_folder_name = tk.StringVar()
            self.cm_destFolder_name = tk.StringVar()
            label = tk.Label(self.pop_cmdir, text="Select the folder:-)", bg="#f5bf69")
            label.grid(row=0,column=0, padx=5, pady=5)
            label1 = tk.Label(self.pop_cmdir, text="Where to paste:-)", bg="#f5bf69")
            label1.grid(row=1, column=0, padx=5, pady=5)
            entery = tk.Entry(self.pop_cmdir, textvariable=self.cm_folder_name, width=50)
            entery.grid(row=0, column=1, padx=5, pady=5)
            entery1 = tk.Entry(self.pop_cmdir, textvariable= self.cm_destFolder_name, width=50)
            entery1.grid(row=1, column=1, padx=5, pady=5)
            button = tk.Button(self.pop_cmdir, text="Browse", command=lambda: self.browse_dir(entery), bg="yellow")
            button.grid(row=0, column=2, padx=5, pady=5)
            button1 = tk.Button(self.pop_cmdir, text="Browse", command=lambda: self.browse_paste(entery1), bg="yellow")
            button1.grid(row=1, column=2, padx=5, pady=5)
            copy_button = tk.Button(self.pop_cmdir, text="Copy", command=self.copy_the_dir)
            copy_button.grid(row=2, column=0, padx=8, pady=8)
            move_button = tk.Button(self.pop_cmdir, text="Move", command=self.move_the_dir)
            move_button.grid(row=2, column=1, padx=8, pady=8)
            exit_button = tk.Button(self.pop_cmdir, text="Exit", command=self.pop_cmdir.destroy)
            exit_button.grid(row=2, column=2, padx=8, pady=8)
            self.pop_cmdir.mainloop()

    def del_the_folder(self):
        self.functionalities_file.delThe_dir(self.del_folder_name.get())

    def del_dir_window(self):
        self.pop_delfolder_window = tk.Frame(self.options_window, bg="#f5bf69")
        self.pop_delfolder_window.place(x=0, y=300)
        self.del_folder_name = tk.StringVar()
        label = tk.Label(self.pop_delfolder_window, text="Select the folder", bg="#f5bf69")
        label.grid(row=0,column=0, padx=5,pady=5)
        entery = tk.Entry(self.pop_delfolder_window, textvariable=self.del_folder_name, width=50)
        entery.grid(row=0, column=1, padx=5, pady=5)
        button = tk.Button(self.pop_delfolder_window, text="Browse", command=lambda: self.browse_paste(entery))
        button.grid(row=0, column=2, padx=5, pady=5)
        del_folder_btn = tk.Button(self.pop_delfolder_window, text="Delete", command=self.del_the_folder)
        del_folder_btn.grid(row=1, column=0, padx=10, pady=10)
        exit_btn = tk.Button(self.pop_delfolder_window, text="Exit", command=self.pop_delfolder_window.destroy)
        exit_btn.grid(row=1, column=1, padx=10, pady=10)
        self.pop_delfolder_window.mainloop()

    def create_options(self):
        self.options_window = tk.Toplevel()
        self.options_window.geometry("650x500")
        copy_file_button = tk.Button(self.options_window, text="Copy or move file", command= self.copy_move_file_window)
        copy_file_button.grid(row=0, column=0, padx=5, pady=5)
        delete_file_button = tk.Button(self.options_window, text="Delete the file", command=self.delete_the_file_window)
        delete_file_button.grid(row=0, column=1, padx=5, pady=5)
        copy_move_dir = tk.Button(self.options_window, text="Copy or move folder", command=self.copy_moveDir_window)
        copy_move_dir.grid(row=1, column=0, padx=(12,0),pady=5)
        delete_folder_button = tk.Button(self.options_window, text="Delete folder", command=self.del_dir_window)
        delete_folder_button.grid(row=1, column=1, padx=5,pady=5)
        self.options_window.mainloop()

    def options_btn(self):
        button = tk.Button(self.options_frame, text='Options', command=self.create_options, font=("Purisa",10,"bold"))
        button.grid(row=0,column=2, pady=5, padx=5)
        return button

    def browse(self):
        file_list = str(filedialog.askdirectory())
        self.directory_name.insert('1',file_list)
        global dir_name
        dir_name = self.name_var.get()

    def orgainzation_done(self):
        temp = Extension_wise(dir_name)
        messagebox.showinfo("info","your directory is organized successfully")

    def organize_window(self):
        self.toplevel = tk.Frame(self.window, bg='white')
        self.toplevel.pack()
        messagebox.showinfo('info', '''Your directory is going to orgainze in this way:-)
                            
1. All files are organized in there respective folders
                            
2. Into that folders all the file further arrange in order to there extension
                            
click on ok to continue
                            ''')
        # self.toplevel.geometry("450x300")
        # global name_var
        self.name_var = tk.StringVar()
        label = tk.Label(self.toplevel, text="Enter the full path of directory", font=("Purisa",12,"bold"), bg='white')
        label.grid(row=0, column=1, padx=5, pady=5)
        # global directory_name
        self.directory_name = tk.Entry(self.toplevel, width=40, textvariable=self.name_var)
        self.directory_name.grid(row=1, column=1, padx=(10,0), pady=5)
        button = tk.Button(self.toplevel, text="Browse", command=self.browse, bg='yellow')
        button.grid(row=1, column=2, padx=5, pady=5)
        button1 = tk.Button(self.toplevel, text="Enter", command= self.orgainzation_done)
        button1.grid(row=3, column=1, padx=(0,100), pady=5)
        button2 = tk.Button(self.toplevel, text="Exit", command=self.toplevel.destroy)
        button2.grid(row=3, column=2, padx=(0,50), pady=5)
        self.toplevel.mainloop()
        

    def organize_btn(self):
        button = tk.Button(self.options_frame, text='Organize Directory', command = self.organize_window, font=("Purisa",10,"bold"))
        button.grid(row=0, column=1, padx=5, pady=5)
        return button
    
    def bottom_img(self):
        frame_img = tk.PhotoImage(file="File_manager_py/gui/box.png")
        myimg = tk.Label(image=frame_img)
        myimg.pack(side="bottom")
        user_label = tk.Label(self.window, text="User:-)", fg="white", bg="#1ab5ef", font=("Purisa",13,"bold"))
        user_label.place(x=80, y=410)
        user_name = self.functionalities_file.user_name()
        os_name = self.functionalities_file.os_name()
        user_name_label = tk.Label(self.window, text=user_name, fg="black", bg="#1ab5ef",  font=("Purisa",13,"bold"))
        user_name_label.place(x=80, y=445)
        os_label = tk.Label(self.window, text="Operating System:-)", fg="white", bg="#1ab5ef", font=("Purisa",13,"bold"))
        os_label.place(x=200, y=410)
        os_name_label = tk.Label(self.window, text=os_name, fg="black", bg="#1ab5ef", font=("Purisa",13,"bold"))
        os_name_label.place(x=200, y=445)
        cwd_name = self.functionalities_file.cwd()
        cwd_label = tk.Label(self.window, text="Current Working directory:-)", fg="white", bg="#1ab5ef", font=("Purisa",13,"bold"))
        cwd_label.place(x=440, y=410)
        cwd_name_label = tk.Label(self.window, text=cwd_name, fg="black", bg="#1ab5ef", font=("Purisa",8,"bold"))
        cwd_name_label.place(x=420, y=445)
        return frame_img

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    filemanager = FileManager_gui()
    filemanager.run()