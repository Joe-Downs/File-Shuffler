import os
import random
import tempfile

directory_string = input("Choose the Folder to Shuffle: ")
directory_byte   = os.fsencode(directory_string)

print()
print("Please choose the extension(s) you wish to be swapped.")
print("Press enter to continue after you have finished input.")
print()

swapped_extension_array = []
answer = " "
swapped_files_count = 0

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

#file_sort() takes a directory path and adds every file and folder's path to the respective arrays
def file_sort(target_dir):
    dir_files  = os.listdir(target_dir)
    for entry in dir_files:
        string_filepath = os.path.join(target_dir, entry)
        #If the path is a directory, add path to dir_array
        #If the path is a file AND the extension has been chosen, add path to file_array
        if os.path.isdir(string_filepath):      
            dir_array.append(string_filepath)
        elif os.path.isfile(string_filepath):   
            if string_filepath.endswith(swapped_extension_tuple):
                file_array.append(string_filepath)

while dir_array != []:
    for directory in dir_array:
        file_sort(target_dir = directory)
        dir_array.remove(directory)

#Prints every entry of the file_array
#print("File Array: " + str(file_array))
#for entry in file_array:
#    print(entry)

#obtain_parent() takes path of file and returns path of folder containing said file
def obtain_parent(filepath): 
    final_separator_index = filepath.rfind("/")
    if final_separator_index == -1:
        final_separator_index = filepath.rfind("\\")
    return filepath[:final_separator_index]

file_swap_calls = 0
#swap_file() takes two filepaths and swaps them
def file_swap(source, destination):
    global swapped_files_count
    global file_swap_calls
    #Do nothing if the source and destination paths are the same
    if source == destination:
        swapped_files_count += 1
        return
    #Removes file from filepath to obtain parent directory
    destination_dir = obtain_parent(destination) 
    tempfile.mkstemp(suffix= ".tempswap", dir=destination_dir)
    destination_dir_files = os.listdir(destination_dir)
    #Search for (hopefully) only file with .tempswap extension
    for entry in destination_dir_files: 
        if entry.endswith(".tempswap"):
             tempfile_filepath = os.path.join(destination_dir, entry)
    os.replace(source, tempfile_filepath)
    os.replace(destination, source)
    os.replace(tempfile_filepath, destination)
    #try:
    #    os.remove(tempfile_filepath)
    #except OSError:
    #    pass
    swapped_files_count += 2
    file_swap_calls += 1
    
#get_extension() taks a filepath and returns the sring value of the filepath's extension (everything after the ".")
def get_extension(filepath):
    extension_begin_index = filepath.rfind(".")
    extension = filepath[extension_begin_index:]
    return extension

while file_array != []:
    for entry in file_array:
        if entry.endswith(swapped_extension_tuple):
            first_extension = get_extension(entry)
            #print()
            #print(entry)
            second_index = random.randint(0, (len(file_array)-1))
            second_extension = get_extension(file_array[second_index])
            #print(file_array[second_index])
            if first_extension == second_extension:
                print("Source: " + str(entry))
                print("Dst:    " + str(file_array[second_index]))
                file_swap(entry, file_array[second_index])
                file_array.remove(entry)
                #Checkpoint print statement every 50 files
                if swapped_files_count % 50 == 0:
                    print(str(swapped_files_count) + " files have been swapped!")
print(file_swap_calls)
