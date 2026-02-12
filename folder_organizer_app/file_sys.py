import os
import shutil

def list_folder_files(folder_path):
    files=os.listdir(folder_path)
    #print(files)
    return files
   #listing all files after inputing the folder path 

def move_files(working_dir,file_name,folder_name):
    destination_path=os.path.join(working_dir,folder_name)
    #destination path exists if it doesnt create one
    source=os.path.join(working_dir,file_name)
    print("Moving file to",destination_path)

    isdir=os.path.isdir(destination_path)

    #creating the folder if it doesnt exist
    if not isdir:
        os.mkdir(destination_path)
    shutil.move(src=source,dst=destination_path)