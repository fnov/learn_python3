#!/usr/bin/python

#Дано целое положительное число из трёх отличных друг от друга цифр.
#Напечатайте "Да", если цифры следуют друг относительно друга в восходящем порядке слева
#направо и "Нет", если это не так.

i = input()

i1 = int(i[0])
i2 = int(i[1])
i3 = int(i[2])

if i1 < i2 < i3:
    o = 'yes'
else:
    o = 'no'

print(o)
