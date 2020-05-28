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
os.makedirs('/run/user/1000/new_dir/sub_dir/sub_dir5')
# os.makedirs(r'C:\delicious\walnut\waffles')  # Windows

# Handling Absolute and Relative Paths
Path.cwd().is_absolute()
os.path.isabs('.')  # old
Path.cwd() / Path('my/relative/path')
Path.home() / Path('my/relative/path')
print(os.path.abspath('new_dir'))
print(os.path.relpath('/run/user/1000', '/home'))
