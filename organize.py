#!/usr/bin/env python3
# Recieves absolute path to a directory as a first CL argument
# Recieves either 'size' or 'ext' as a second argument and organizes according to that
# creates folders in a directory for each group
# example:
# ./orginize.py /home/usr/Desktop/folder ext

import sys
import os
import shutil
import send2trash
zxc
# Parse arguments
if len(sys.argv) < 3:
    print("Usage: organize.py <absolute_path> <size|ext>")
    sys.exit()

folder = sys.argv[1]
mode = sys.argv[2]

if not os.path.isabs(folder):
    print("First argument must be an absolute path.")
    sys.exit()

if mode not in ('size', 'ext'):
    print("Second argument must be either 'size' or 'ext'")
    sys.exit()

#returns extension as a string when file name is passed as an argument
def getExtension(file):
    _, extension = os.path.splitext(file)
    extension = extension.lstrip('.')
    if extension == '':
        extension = 'no_extension'
    return extension

# if files are to be sorted based on their extensions, for each file code checks if a folder with a name of the extension
# has already been created, if not, it creates one and moves the file to it 
if mode == 'ext':
    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)
        if os.path.isfile(full_path):
            extension = getExtension(file)
            target_dir = os.path.join(folder, extension)
            if not os.path.exists(target_dir):
                os.mkdir(target_dir)
            shutil.move(full_path, os.path.join(target_dir, file))

if mode == 'size':
    subFolder1 = os.path.join(folder, '0-100MB')
    subFolder2 = os.path.join(folder, '100-300MB')
    subFolder3 = os.path.join(folder, '300-500MB')
    subFolder4 = os.path.join(folder, '500-700MB')
    subFolder5 = os.path.join(folder, '700-900MB')
    subFolder6 = os.path.join(folder, '900-1GB')
    subFolder7 = os.path.join(folder, '1GB+')

    for subfolder in [subFolder1, subFolder2, subFolder3, subFolder4, subFolder5, subFolder6, subFolder7]:
        if not os.path.exists(subfolder):
            os.mkdir(subfolder)

    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)
        if os.path.isfile(full_path):
            sizeMB = os.path.getsize(full_path) / 1000000
            if sizeMB <= 100:
                target_dir = subFolder1
            elif sizeMB <= 300:
                target_dir = subFolder2
            elif sizeMB <= 500:
                target_dir = subFolder3
            elif sizeMB <= 700:
                target_dir = subFolder4
            elif sizeMB <= 900:
                target_dir = subFolder5
            elif sizeMB <= 1000:
                target_dir = subFolder6
            else:
                target_dir = subFolder7

            shutil.move(full_path, os.path.join(target_dir, file))
    for subfolder in os.listdir(folder):
        subfolder_path = os.path.join(folder, subfolder)
        if os.path.isdir(subfolder_path) and len(os.listdir(subfolder_path)) == 0: 
            send2trash.send2trash(subfolder_path)

print('done')
sys.exit()
