"""
Warning:
I don't know what I'm doing

This program will change file permissions to 644 in octal 0o644
                and directory permissions to 755 in octal 0o755
Only in the directory where it is run.
I hope.
Don't use this for anything.
"""
import os
dl = list()
fl = list()

def set_file_permissions(l):
    for file in l:
        os.chmod(file, 0o644, follow_symlinks=False)

def set_directory_permissions(l):
    for directory in l:
        os.chmod(directory, 0o755, follow_symlinks=False)

def recurse_directories(l):
    # recurse through directory tree and build/return list of directories
    for directory in l:
        os.chdir(directory)
        get_directories()
    return l

def recurse_files(l):
    # recurse through directory tree and build/return list of files only
    for directory in l:
        os.chdir(directory)
        get_files()
    return l

def get_directories():
    # !returns a list of the abspath of directories in the current cwd.
    #l = list()
    global dl
    contents = os.listdir()
    for directory in contents:
        if os.path.isdir(directory):
            dl.append(f'{os.getcwd()}/{directory}/')
    return dl

def get_files():
    # !returns a list of the abspath of all files in the cwd
    global fl
    contents = os.listdir()
    for file in contents:
        if os.path.isfile(file):
            fl.append(f'{os.getcwd()}/{file}')
    return fl

# recurse_directories(l)
# print(recurse_files(bleh))
# l = get_directories()
# print(recurse_directories(l))
# file_list = get_files()
# set_file_permissions(file_list)
# set_directory_permissions(directory_list)
# d = get_directories()
# f = get_files()
# print(recurse_files(d))
