#!/usr/bin/python

#Дано целое положительное число.
#Напечатайте "чёт", если число чётное и "нечет", если число нечётное.

i = int(input())

if i % 2 == 0:
    o = 'chetnoe'
else:
    o = 'nechetnoe'

print(o)
