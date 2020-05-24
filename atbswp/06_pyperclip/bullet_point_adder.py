#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""bullet_point_adder.py - Adds Wikipedia bullet points to the start
of each line of text on the clipboard."""

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i, line in enumerate(lines):  # loop through all indexes in the "lines" list
    lines[i] = '* ' + line        # add star to each string in "lines" list

text = '\n'.join(lines)
pyperclip.copy(text)
