from typing import final
from PIL import Image
from os import listdir, getcwd, mkdir
from os.path import isfile, join
from sys import argv

def compile_file_dictionary(root_folder):
    all_directories = []

    # Counts number of directories
    dir_count = 0
    for f in listdir(root_folder):
        if not isfile(join(root_folder, f)) and f != 'finals':
            dir_count += 1
            all_directories.append(f)

    file_dictionary = {}

    for dir in all_directories:
        dir_full_path = root_folder + dir
        all_files_in_dir = [f for f in listdir(dir_full_path) if isfile(join(dir_full_path, f)) and f != '.DS_Store']
        file_dictionary[dir] = all_files_in_dir

    return(file_dictionary)

def dfs_dict(key_num):

    print('\n\nfunction')
    for i in f_dict[keys[key_num]]: ## f_dict inhabits global scope (not modular)

        img_layers.append(join(keys[key_num], i))

        #if stack full (at max depth)
        ## at leaf node
        if len(img_layers) == len(f_dict):
            img_count[0] += 1
            compressor(img_layers, img_count)
            print(img_layers) # printing press
            img_layers.pop()

        # if stack not full
        elif len(img_layers) < len(f_dict):
            print('not max')
            # Traverse adjacent edges
            dfs_dict(key_num + 1) # Only works on ordered dictionaries (3.7+)
            img_layers.pop()
        else:
            raise ValueError('Out of range in dfs_dict')

def compressor(files, name):
    # Gutenberg Press

    for i in range(0, len(files) - 1):
        backImg = Image.open(join(root_folder, files[i]), mode='r')
        frontImg = Image.open(join(root_folder, files[i+1]), mode='r')

        backImg.paste(frontImg, (0,0), frontImg)
    backImg.save(final_folder + str(name[0]) + '.png')
    print(final_folder + str(name[0]) + '.png')

root_folder = ''

# if len(argv) == 0:
#     root_folder = getcwd() + '/'
# else:
#     root_folder = str(argv[1])

root_folder = '/Users/admin/Desktop/w/'
final_folder = root_folder + 'finals/'

try:
    mkdir(final_folder)
except OSError as e:
    print('folder already created!')
    print(e)

f_dict = compile_file_dictionary(root_folder=root_folder)
print(f_dict)
## n-ary depth first tree traversal
## (where we know the tree depth)

### Needed for dfs_dict to run
img_layers = []
keys = list(f_dict.keys())
img_count = [0]
###

dfs_dict(0)