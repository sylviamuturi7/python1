import os
import sys
def get_user_folder():
    folder_path=input("Enter the folder path: ")
    print(folder_path)
    isdir=os.path.isdir(folder_path)
    #is false ->notfalse -> true 
    #The answer for isdir is either true or false (datatype is boolean)
    
    if not isdir:
        print("Invalid folder path")
        sys.exit() #exits the folder path
    return folder_path

        
#return exits a funcion
    #os.path,isdir() method is used to check whether the specified path is an existing directory or not.