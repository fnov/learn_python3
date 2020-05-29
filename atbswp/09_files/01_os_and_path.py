#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os  # os.path is old
from pathlib import Path  # modern

# use raw strings for Windows
print(r'c:\spam\eggs.png')

# joining path
print(Path('spam', 'bacon', 'eggs'))  # spam/bacon/eggs
Path('spam') / 'bacon' / 'eggs'  # same
Path('spam') / Path('bacon/eggs')  # same
os.path.join('spam', 'bacon', 'eggs')  # old

# current working directory (cwd or pwd)
print(Path.cwd())
print(os.getcwd())  # old

# cd
os.chdir('/run/user/1000')

# path for ~ (C:/Users/%username% for Windows)
print(Path.home())

# mkdir (can -p)
path0 = Path('/run/user/1000/new_dir/sub_dir/sub_dir2')
if not path0.exists():
    os.makedirs(path0)
# os.makedirs(r'C:\delicious\walnut\waffles')  # Windows

# Handling Absolute and Relative Paths
Path.cwd().is_absolute()
os.path.isabs('.')  # old
Path.cwd() / Path('my/relative/path')
Path.home() / Path('my/relative/path')
print(os.path.abspath('new_dir'))
print(os.path.relpath('/run/user/1000', '/home'))

"""The parts of a file path include the following:
    The anchor, which is the root folder of the filesystem
    On Windows, the drive, which is the single letter that often denotes a physical hard drive or other storage device
    The parent, which is the folder that contains the file
    The name of the file, made up of the stem (or base name) and the suffix (or extension)
"""
path1 = Path('/etc/apt/sources.list')
print(path1.anchor)
parent = path1.parent
print(parent)  # This is a Path object, not a string
os.path.dirname(path1)  # old
print(path1.name)
os.path.basename(path1)  # old
print(path1.stem)
print(path1.suffix)
print(*path1.parents)  # may use parents[0], parents[1] etc.

# split dirname and basename
os.path.split(path1)  # ('/etc/apt', 'sources.list')
# so you can
folder, fname = os.path.split(path1)

# validating
path1.exists()
os.path.exists(path1)  # old
path1.is_dir()
os.path.isdir(path1)  # old
path1.is_file()
os.path.isfile(path1)  # old

# get size of file
os.path.getsize('/etc/apt/sources.list')  # in bytes

# ls
os.listdir('/tmp')
# or using Path.glob()
list(parent.glob('*'))  # Make a list from the generator.
list(parent.glob('*.list'))

total_size = 0
for filename in parent.glob('*'):
    total_size += os.path.getsize(str(filename))
print(total_size)
