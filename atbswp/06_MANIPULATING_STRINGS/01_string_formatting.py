#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""PEP 498 -- Literal String Interpolation
https://www.python.org/dev/peps/pep-0498/ """

name = 'Al'
age = 4000

# %-formatting https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
print('My name is %s. I am %s years old.' % (name, age))

# str.format() https://docs.python.org/3/library/string.html#formatstrings
print('My name is {}. Next year I will be {}.'.format(name, age))

# str.format() examples

# Accessing arguments by position:
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format(*'abc'))  # unpacking argument sequence
print('{0}{1}{0}'.format('abra', 'cad'))  # arguments' indices can be repeated
# Accessing arguments by name:
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))
# Expressing a percentage:
points = 19
total = 22
print('Correct answers: {:.2%}'.format(points/total))
# Accessing arguments’ attributes:
c = 3-5j
print('The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.'.format(c))


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)


print(str(Point(4, 2)))
# Aligning the text and specifying a width:
print('{:<30}'.format('left aligned'))
print('{:>30}'.format('right aligned'))
print('{:^30}'.format('centered'))
print('{:*^30}'.format('centered'))  # use '*' as a fill char)
# format also supports binary numbers
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
# with 0x, 0o, or 0b as prefix:
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))

octets = [192, 168, 0, 1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))

width = 5
for num in range(5, 12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()

# Python 3.6 introduced f-strings
print(f'My name is {name}. Next year I will be {age + 1}.')
