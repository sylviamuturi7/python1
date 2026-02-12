#def main():
 #   print("main function is coming soon")
#main()

from user_folder import get_user_folder
from file_sys import list_folder_files,move_files
import os

IMAGES=["jpg","jpeg","png"]
MUSIC=["mp3","wav"]
PDF=["pdf"]
ZIP=["tar","zip","rar"]


def main():
    print("Welcome to Folder Organizer App")    
    print("_________________________________")
    working_folder=get_user_folder()
    items=list_folder_files(working_folder)

    for item in items:
        print("single item is",item)
        split_item=os.path.splitext(item)
        #print("split item is",split_item)
        #print("first element",split_item[0])
        #print("second element",split_item[1])
        extension=split_item[1]
        folder_name="other"

        if extension in IMAGES:
            print("f is file (item) its an image")
            folder_name="images"
        elif extension in MUSIC:
            print("f is file (item) its a music")
            folder_name="music"
        elif extension in PDF:
            print("f is file (item) its a pdf")
            folder_name="pdf"
        elif extension in ZIP:
            print("f is file (item) its a zip")
            folder_name="zip"
        else:
            print("f is file (item) its in others or unknown")
            folder_name="other"
    print("The folder name is",folder_name)
    move_files(working_folder,item,folder_name)
        
main()