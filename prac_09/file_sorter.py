import os
import shutil

print("Current directory is", os.getcwd())

#change to Files to Sort
os.chdir('FilesToSort')
print("Current directory is", os.getcwd())
directory_names = []

# for filename in os.listdir('.'):
#     directory_name = os.path.splitext(filename)[1]
#     if directory_name not in directory_names:
#         os.mkdir(directory_name)
#         directory_names.append(directory_name)
#
     # shutil.move(filename,directory_name)

# filetypes = []


# /files = os.listdir('.')
filetypes = []

types = {}
for file in os.listdir('.'):
    filetype = os.path.splitext(file)[1]
    if filetype not in filetypes:
        filetypes.append(filetype)
        directory_name = input("What category would you like to sort {} into?".format(filetype))
        types[filetype]=directory_name

    for value in types.values():
        if value not in directory_names:
            os.mkdir(value)
            directory_names.append(value)

    for key, a in types.items():
        if key == filetype:
            shutil.move(file,a)

    print("Current directory is", os.getcwd())










