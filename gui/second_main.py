'''
author:- @kishan_chauhan

problem_statement:- making file-managment system
level1:-move files to there respective folder like if is there any img file than move to image folder and if ther any video 
file then move to video folder like this. And don't do anything to folders if is there.
level2:- organizes all the files in there respective folder by date wise or a-z or z-a.// Give this functionality to user so
user can decide in GUI
level3:-Make GUI of this things via tkinter
'''
import os
import shutil

def check_extension(extensions):
    '''This function check all extensions, if there is any extensions that belongs to folder than it will remove by this function'''
    global image_extension
    image_extension = ['.webp','.jpg','.jpeg','.svg','.psd','.gif','.png']
    global video_extension
    video_extension= ['.mp4','.mkv','.webm','.flv','.avi','.mpeg']
    global audio_extension
    audio_extension = ['.mp3','.wav','.flac','.aac']
    global document_extension
    document_extension = ['.pdf','.pptx','.docx','.xlsx','.txt','.html','.css','.json','.js','.ipynb']
    global compressed_extention
    compressed_extention = ['.zip' , '.rar', '.7z' , '.tar.gz', '.tgz', '.tar', '.tar.xz','.deb']
    global software_extension
    software_extension = ['.EXE','.exe']
    
    proper_extensions = []
    for i in range(len(extensions)):
        if(extensions[i] in image_extension):
            proper_extensions.append(extensions[i])
        elif(extensions[i] in video_extension):
            proper_extensions.append(extensions[i])
        elif(extensions[i] in audio_extension):
            proper_extensions.append(extensions[i])
        elif(extensions[i] in document_extension):
            proper_extensions.append(extensions[i])
        elif(extensions[i] in compressed_extention):
            proper_extensions.append(extensions[i])
        elif(extensions[i] in software_extension):
            proper_extensions.append(extensions[i])
 
    return proper_extensions

def split_extensions(all_items):
    '''This function will split the extensions from file name and return a list of extensions present in download directory'''
    extensios = []
    for i in range(len(all_items)):
        base_name, after_dot = os.path.splitext(all_items[i])
        extensios.append(after_dot)
    return extensios

def checking_creatingFolder(all_items):
    '''This function will check that how many respective folder have to make for there files and return a set'''
    #$$--> update this one on deployment
    folder_names = set()
    
    for i in range(len(all_items)):
        if(all_items[i] in image_extension):
            folder_names.add("images")
        elif(all_items[i] in video_extension):
            folder_names.add("videos")
        elif(all_items[i] in audio_extension):
            folder_names.add("audios")
        elif(all_items[i] in document_extension):
            folder_names.add("documents")
        elif(all_items[i] in compressed_extention):
            folder_names.add("compressed")
        elif(all_items[i] in software_extension):
            folder_names.add("softwares")
    
    return folder_names


def moving_fileName(all_items):
    '''This function append files in there respective lists and return None because here
        I'm make change directly in global variable
    '''
    global image_file
    image_file = []
    global video_file 
    video_file = []
    global audio_file
    audio_file = []
    global document_file
    document_file = []
    global compressed_file
    compressed_file = []
    global software_file
    software_file = []
    
    for i in range(len(all_items)):
        if(all_items[i].endswith(tuple(image_extension))):
            image_file.append(all_items[i])
        elif(all_items[i].endswith(tuple(video_extension))):
            video_file.append(all_items[i])
        elif(all_items[i].endswith(tuple(audio_extension))):
            audio_file.append(all_items[i])
        elif(all_items[i].endswith(tuple(document_extension))):
            document_file.append(all_items[i])
        elif(all_items[i].endswith(tuple(compressed_extention))):
            compressed_file.append(all_items[i])
        elif(all_items[i].endswith(tuple(software_extension))):
            software_file.append(all_items[i])
    
    return None
def move_files():
    '''This function move the files in there respective directories '''
    # main_path = '/home/kishan/Downloads/'
    for i in range(len(image_file)):#for images
        shutil.move(os.path.join(main_path,image_file[i]), os.path.join(main_path, 'images'))
    print("images done")
    for i in range(len(video_file)):#for images
        shutil.move(os.path.join(main_path,video_file[i]), os.path.join(main_path, 'videos'))
    print("video done")
    for i in range(len(audio_file)):#for images
        shutil.move(os.path.join(main_path,audio_file[i]), os.path.join(main_path, 'audios'))
    print("audio done")
    for i in range(len(document_file)):#for images
        shutil.move(os.path.join(main_path,document_file[i]), os.path.join(main_path, 'documents'))
    print("documents done")
    for i in range(len(compressed_file)):#for images
        shutil.move(os.path.join(main_path,compressed_file[i]), os.path.join(main_path, 'compressed'))
    print("compressed done")
    for i in range(len(software_file)):#for images
        shutil.move(os.path.join(main_path,software_file[i]), os.path.join(main_path, 'softwares'))
    print("software done")
    
    
if __name__ == '__main__':
    main_path = '/home/kishan/Downloads/'
    list_items = os.listdir(main_path)
    #store the extensions
    
    splited_extensions = split_extensions(list_items)

    #removing folder in extension if folder name ends with dot (.sample) like this formate
    correct_extensions = check_extension(splited_extensions)
    print(correct_extensions)

    '''If is there any kind of folder than we are not going to do any thing to that folder'''
    folder_making = list(checking_creatingFolder(correct_extensions))
    '''creating folders'''
    for i in range(len(folder_making)):
        path = os.path.join(main_path, folder_making[i])
        if os.path.exists(path):
            print('already exist')
        else:
            os.mkdir(path)
            print("path created")
    print(folder_making)
    moving_fileName(list_items)
    
    '''moving the files'''
    move_files()
    