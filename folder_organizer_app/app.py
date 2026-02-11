#def main():
 #   print("main function is coming soon")
#main()

from user_folder import get_user_folder
from file_sys import list_folder_files

IMAGES=["jpg","jpeg","png"]
MUSIC=["mp3","wav"]
PDF=["pdf"]
ZIP=["tar","zip","rar"]


def main():
    print("Welcome to Folder Organizer App")    
    print("_________________________________")
    working_folder=get_user_folder()
    items=list_folder_files(working_folder)
main()