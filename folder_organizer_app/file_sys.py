import os
def list_folder_files(folder_path):
    files=os.listdir(folder_path)
    print(files)
    return files
   #listing all files after inputing the folder path 