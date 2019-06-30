import os
directory_input = input("Choose the Folder to Shuffle: ")
directory = os.fsencode(directory_input)

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

#Folder class to store information about each subfolder (no. of files, filetypes, filenames)
class Folder:
#Can a class reference an array?

#Function(s) to gather information about each subfolder and initialize an instance of Folder
def init_Folder:

def gather_info:
