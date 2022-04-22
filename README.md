# Layer Combinator

## Introduction

The code can be used to produce images from all combinations of provided layers.

## Requirements
- Layers need to be placed in the appropriate folder structure (mentioned below)
- Layers need to be in a compatible format (PNG - more can be found in the Pillow
  Library)
- Pillow (tested on version: 9.1.0) needs to be installed
- Python 3.7+

## Folder Structure

> Note: Any number of images in each folder will work!

> Note: Folder order matters because the layer order will follow the folder order.
      It follows os.walk pattern. In case they need to be reordered, simply add
      numbers to the folder name. For example, if I want my hat layer to be the
      top most layer, followed by subject and lastly the background, the folder
      names could be as follows: "1 - Hat", "2 - Subject", and "3 - Background".

Root Folder
  - Layer 1 Folder
    - Layer 1 Image 1
    - Layer 1 Image 2
    - Layer 1 Image 3
    - Layer 1 Image 4
  - Layer 2 Folder
    - Layer 2 Image 1
    - Layer 2 Image 2
    - Layer 2 Image 3
  - Layer 3 Folder
    - Layer 3 Image 1
    - Layer 3 Image 2
    - Layer 3 Image 3

Example:

Root Folder
  - Hat Folder
    - Subject Hat 1 (Black Hat)
    - Subject Hat 2 (Purple Hat)
    - Subject Hat 3 (Orange Hat)
    - Subject Hat 4 (Yellow Hat)
  - Subject Folder
    - Subject 1 (Red Alien)
    - Subject 2 (Blue Alien)
    - Subject 3 (Green Alien)
  - Background Folder
    - Background 1 (Mars)
    - Background 2 (Earth)
    - Background 3 (Spaceship)

Final images can be found in the directory 'finals/' in the root folder.

## How To Use

*Pre-execution:*
*Make sure you're running Python in an environment where pillow is installed.*
*Ensure the appropriate folder structure of the layer images is followed.*

Step 1: Open the code and replace the path on line 68 with the path to your
root folder.

Optional: Replace `root_folder + 'finals/'` with the path to where your finals
folder should be.

Step 2: Switch into the directory that has the code and execute the script by
running:

> Note: These may vary depending on your environment.

MacOS: `python layer-combinator.py`
Windows: `py layer-combinator.py`


## How It Works

First, the code parses the root folder and compiles a dictionary that holds the
image paths for each layer. Then, this feeds into the main mechanism behind the
code; a recursive function that implements a depth first search on an n-ary tree.
When the code reaches a leaf, the function sends a stack of layers to a function
that uses the pillow library to compile all images into a single result. This
is repeated until the entire tree is exhausted.

## Extra

The code also supports giving the root folder path as a command line argument.
To enable this uncomment lines 63-66, and comment line 68. Once this is done,
the code will assume the current directory is the root folder, unless a path is
given as argument 1.
