import os
import random

#Program Outline
#1 Prompt user to select directory and extension
#  --Allow recursive / non-recursive options (argparse?)
#2 Iterate through each file / folder in the directory, adding each file and folder's full paths to a respective array
#3 Choose first entry in the file and a random file (of the same extension) elsewhere in the array (could be the first one)
#  --If the same file, skip to #8
#4 Create temp file in destination [tempfile.mkstemp()]
#5 Move file 1 to temp file path in destination [os.replace()]
#6 Move file 2 to file 1 path [os.rename()]
#7 Rename temp file to file 2
#8 Remove the two entries from the filepath array

directory_string = input("Choose the Folder to Shuffle: ")
directory_byte   = os.fsencode(directory_string)

print("\nPlease choose the extension(s) you wish to be swapped.\nPress enter to exit after you have finished input.\n")

swapped_extension_array = []
answer = " "

#Prompt reappears after each input until the user hits enter on the blank field
while answer != "":
    answer = input("Which extensions do you want swapped? ")
    if answer != "":
        swapped_extension_array.append(answer)

print("Chosen Extensions: " + str(swapped_extension_array))

#dir_array must be declared with the initial path, else the program will result in an endless loop
dir_array  = [directory_string]
file_array = []
#Tuple of extension array initialized AFTER the extensions are chosen
swapped_extension_tuple = tuple(swapped_extension_array)

#Function to sort a given directory and add directory / files to the respective array
def file_sort(target_dir):
    dir_files  = os.listdir(target_dir)
    for entry in dir_files:
        #os.path.join()
        if target_dir.endswith("/"):
            string_filepath = str(target_dir + entry)
        else:
            string_filepath = str(target_dir + "/" + entry)
            
        if os.path.isdir(string_filepath):      #If the path is a directory, add path to dir_array
            dir_array.append(string_filepath)
        elif os.path.isfile(string_filepath):   #If the path is a file AND the extension has been chosen, add path to file_array
            if string_filepath.endswith(swapped_extension_tuple):
                file_array.append(string_filepath)

while dir_array != []:
    for directory in dir_array:
        file_sort(target_dir = directory)
        dir_array.remove(directory)

#print("File Array: " + str(file_array))
for entry in file_array:
    print(entry)


#Only swap files of the same extension
#Need to swap files

"""
def file_swap(source, destination, extension):
    destination_extension =
    while

#tempfile.mkstemp()

for entry in file_array:
    for extension in swapped_extensions:
        file_swap(entry, file_array[random.randint(0, (len(file_array)-1), extension)
"""
