
import os 
import shutil
import tkinter as tk
from tkinter import filedialog
import ldclient
from ldclient.config import Config


# get the directory of existing files - path must be filled in with the location of the saved "Old" directory
BASE_DIR = os.path.dirname("C:/foo/Old/")

root = tk.Tk()
root.withdraw()
#replace SDK here
sdk_key = " "
  

def main(): 
   i = 0
   
   ldclient.set_config(Config(sdk_key))
   client = ldclient.get()
   
   #please edit user name and email below
   user = {
    "key": "testuser1234",
    "firstName": "John",
    "lastName": "Tester",
    "email": "tests@gmail.com"
}
   
   show_feature = client.variation("new-directory-selection",user, False)

   
   if show_feature:
       NEW_DIR = filedialog.askdirectory()
   else:
       #Set the path to the new directory where you would like to save the files
       NEW_DIR = "C:foo/New"

   for filename in os.listdir(BASE_DIR):
        extension = filename[-3:]

        new_file_name = filename[:5] + "_NEW." + extension
        new_file_name = os.path.join(NEW_DIR, new_file_name)

        if not os.path.isfile(new_file_name):
            print(new_file_name)
            os.rename(os.path.join(BASE_DIR, filename), new_file_name)
        else:
            print("file already exists: " + new_file_name)

if __name__ == '__main__': 

    main() 
