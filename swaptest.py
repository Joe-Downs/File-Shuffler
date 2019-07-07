import os
directory_string = input("Choose the Folder to Shuffle: ")
directory_byte   = os.fsencode(directory_string)

print("\nPlease choose the extension(s) you wish to be swapped.\nPress enter to exit after you have finished input.\n")

swapped_extensions = []
answer = " "

#Prompt reappears after each input until the user hits enter on the blank field
while answer != "":
    answer = input("Which extensions do you want swapped? ")
    if answer != "":
        swapped_extensions.append(answer)

print("Chosen Extensions: " + str(swapped_extensions))

#destination = input("Choose the Destination for the Shuffled Directory: ")

#dir_array must be declared with the initial path, else the program will result in an endless loop
dir_array  = [directory_string]
file_array = []

#Function to sort a given directory and add directory / files to the respective array
def file_sort(target_dir):
    dir_files  = os.listdir(target_dir)
    for entry in dir_files:
        if target_dir.endswith("/"):
            string_filepath = str(target_dir + entry)
        else:
            string_filepath = str(target_dir + "/" + entry)
            
        if os.path.isdir(string_filepath):      #If the path is a directory, add path to dir_array
            dir_array.append(string_filepath)
        elif os.path.isfile(string_filepath):   #If the path is a file, add path to file_array
            file_array.append(string_filepath)

while dir_array != []:
    for directory in dir_array:
        file_sort(target_dir = directory)
        dir_array.remove(directory)

print("File Array: " + str(file_array))

###Idea Two
#1 Rename and move at same time
#2 Remove moved path from file_array

#Only swap files of the same extension
#Need to swap files

def file_swap(original, destination, extension):
