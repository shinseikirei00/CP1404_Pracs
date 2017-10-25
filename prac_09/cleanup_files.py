"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os
import shutil

print("Current directory is", os.getcwd())

# change to desired directory
os.chdir('Lyrics')
# print a list of all files (test)
# print(os.listdir('.'))

# make a new directory
# os.mkdir('temp')

# loop through each file in the (original) directory
for dir_name, subdir_list, file_list in os.walk('.'):
# for filename in os.listdir('.'):
    for f in file_list:
    # ignore directories, just process files
        if not os.path.isdir(f):
            new_name = f.replace(" ", "_").replace(".TXT", ".txt")
            print(new_name)

            # # Option 1: rename file to new name - in place
            # os.rename(filename, new_name)
            #
            # # Option 2: move file to new place, with new name (import shutil first)
            # shutil.move(filename, 'temp/' + new_name)


# Processing subdirectories using os.walk()
# os.chdir('..')
# for dir_name, subdir_list, file_list in os.walk('.'):
#     print("In", dir_name)
#     print("\tcontains subdirectories:", subdir_list)
#     print("\tand files:", file_list)