import ctypes
import os
import random

# CONSTANTS --------------------------------------------------------------------------------------
# Edit this value for the number of images you have!


def set_wallpaper(image_path):
    # Ensure the path is absolute
    abs_image_path = os.path.abspath(image_path)
    
    # Change the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_image_path, 0)

# Replace 'path_to_your_image.jpg' with the path to your image file

import os

# Specify the folder path
folder_path = 'Wallpapers'  # Replace with your folder path
prefix = 'X'  # Replace with the prefix you want to add to each file name

# Ensure the folder path is absolute
abs_folder_path_1 = os.path.abspath(folder_path)

# List all files in the folder
files = os.listdir(abs_folder_path_1)

for file_name in files:
    # Skip directories
    if os.path.isdir(os.path.join(abs_folder_path_1, file_name)):
        continue

    # Create the new file name
    new_file_name_prefix = f"{prefix}_{file_name}"

    # Get the full paths
    old_file_path_prefix = os.path.join(abs_folder_path_1, file_name)
    new_file_path_prefix = os.path.join(abs_folder_path_1, new_file_name_prefix)

    # Rename the file
    os.rename(old_file_path_prefix, new_file_path_prefix)
    print(f'Renamed: {old_file_path_prefix} -> {new_file_path_prefix}')


image_counter = 0

abs_folder_path = os.path.abspath(folder_path)

files = os.listdir(abs_folder_path_1)

for file_name in files:
    # Skip directories
    if os.path.isdir(os.path.join(abs_folder_path, file_name)):
        continue

    # Create the new file name
    new_file_name = str(image_counter) + ".png"

    # Get the full paths
    old_file_path = os.path.join(abs_folder_path, file_name)
    new_file_path = os.path.join(abs_folder_path, new_file_name)

    # Rename the
    # file
    os.rename(old_file_path, new_file_path)
    print(f'Renamed: {old_file_path} -> {new_file_path}')


    image_counter += 1

number = random.randint(0, image_counter-1)


filename = str(number) + ".png"
source = "Wallpapers/" + filename
set_wallpaper(source)
print(source)