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

dir_files  = os.listdir(directory_string)
dir_array  = []
file_array = []
print("Directory Files: " + str(dir_files))

#Need to have input for which directory to sort
def file_sort():
    for entry in dir_files:
        if directory_string.endswith("/"):
            string_filepath = str(directory_string + entry)
        else:
            string_filepath = str(directory_string + "/" + entry)
            
        if os.path.isdir(string_filepath): #If the path is a directory, add path to dir_array
            dir_array.append(string_filepath)
        elif os.path.isfile(string_filepath):#If the path is a file, add path to file_array
            file_array.append(string_filepath)
file_sort()

print("Directory Array: " + str(dir_array))
print("File Array: " + str(file_array))

while dir_array != []:
    for directory in dir_array:
        print(directory)
        file_sort()
        dir_array.remove(directory)
        print(dir_array)
        
        
