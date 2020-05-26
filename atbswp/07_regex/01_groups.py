#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.')

print(mo.group())   # '415-555-4242'
print(mo.group(0))  # same as above
print(mo.group(1))  # '415'
print(mo.group(2))  # '555-4242'

print(mo.groups())  # ('415', '555-4242')
areaCode, mainNumber = mo.groups()
print(areaCode)     # '415'
print(mainNumber)   # '555-4242'
