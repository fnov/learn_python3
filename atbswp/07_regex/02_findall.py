#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


def print_findall(pattern):
    print(pattern.findall('Cell: 415-555-9999 Work: 212-555-0000'))


phoneNumRegex1 = re.compile(r'\d{3}-\d{3}-\d{4}')  # has no groups
print_findall(phoneNumRegex1)  # ['415-555-9999', '212-555-0000']

# If there are 2 or more groups in the regular expression, then findall() will return a list of tuples.
phoneNumRegex2 = re.compile(r'(\d{3})-(\d{3}-\d{4})')  # has 2 groups
print_findall(phoneNumRegex2)   # [('415', '555-9999'), ('212', '555-0000')]

phoneNumRegex3 = re.compile(r'((\d{3})-(\d{3}-\d{4}))')
print_findall(phoneNumRegex3)  # [('415-555-9999', '415', '555-9999'), ('212-555-0000', '212', '555-0000')]
