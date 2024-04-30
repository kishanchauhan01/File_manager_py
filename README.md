

# File Manager
* I made this basic file manager with python.
* I used standard `GUI` library called tkinter.
* I make two option in this file manager:-
    1. Organize the directory
    2. Options

* In `Organize button` you have to provide a directory path you want to organize or you can also browse the directories
* Yor dirctory is going to organize in the following ways:-
    1. Firstly all your files like image, video, compressed, document files like pdf, doc, excel, etc. are moved to there respective folders
    2. After that let say in your image folder you have jpg, png, svg, jpeg, etc. files are further moved to there respective extension wise folders
    3. Like wise the processing is going on. And after that you can easly access your files
    4. `Note:- ` If in your dirctory is there any kind of folder or subdirctory then is not going to move any where else so don't worry.

* In `Options` button you have option to copy, cut, delete like features.

# How to use or run the code

1. Just download the zip file on clicking the code button in git hub.
2. After that unzip the zip file and open the `File_manager_py` folder in your `vs code` or any other code editor.
3. After that open the `main_GUI.py` and go to the line no. 380 and after that in your `File_manager_py` folder you have a box.png just copy the file path of that file and past in line no. 380 in the string for example:-
    ``` frame_img = tk.PhotoImage(file="/home/kishan/Desktop/kishan/python/file_managment/File_manager_py/Main_files/box.png") ```
   * you have to past the path of the image file here in the string just after `file=` here file is the variabel name.

🙂 You are done now jsut run the `app.py` file.
