import os
directory_string = input("Choose the Folder to Shuffle: ")
directory_byte   = os.fsencode(directory_input)

print("\nPlease choose the extension(s) you wish to be swapped.\nPress enter to exit after you have finished input.\n")

swapped_extensions = []
answer = " "

#Prompt reappears after each input until the user hits enter on the blank field
while answer != "":
    answer = input("Which extensions do you want swapped? ")
    if answer != "":
        swapped_extensions.append(answer)

print(swapped_extensions)

#Empty arrays to preserve original filenames for later renaming of new files after move
folder_one_filenames   = []
folder_two_filenames   = []
folder_three_filenames = []

working_dir = directory_string

#Folder class to store information about each subfolder (no. of files, filetypes, filenames)
class Folder:
    def __init__(self,
                 filepath):
        self.filepath = filepath
        self.files    = []
    def add_file(self, file)
    
#Can a class reference an array?

#Function(s) to gather information about each subfolder and initialize an instance of Folder
#init_Folder initializes a new instance of folder
def init_Folder():
    
#Functions called again if folder has_subfolder = true
