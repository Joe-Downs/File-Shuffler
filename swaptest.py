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

working_dir = directory_string

#Folder class to store information about each subfolder (no. of files, filetypes, filenames)
class Folder:
    def __init__(self, filepath):
        self.filepath   = filepath
        self.filenames  = []
        self.file_count = 0
        
    def add_filename(self, filename):
        self.filenames.append(filename)

    def count_files(self):
        self.file_count = len(self.filenames)

    def display_names(self):
        print(self.filenames)

    def display_count(self):
        print(self.file_count)
    

#Function(s) to gather information about each subfolder and initialize an instance of Folder
#init_Folder initializes a new instance of folder
def init_Folder():
    
#Functions called again if folder has_subfolder = true
