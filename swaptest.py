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


#For each folder and file in a directory, adds full path to either folder array or file array
dir_array  = [directory_string]
file_array = []

#Need to have input for which directory to sort
def file_sort(target_dir):
    dir_files  = os.listdir(target_dir)
   #print("Directory Files: " + str(dir_files))
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

print("Directory Array Final: " + str(dir_array))
print("Directory Array: " + str(dir_array))
print("File Array: " + str(file_array))
