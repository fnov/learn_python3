#!/usr/bin/python

#Дано целое число из трёх цифр.
#Напечатайте сумму цифру числа.

number = input()
s = 0
for i in number:
    s += int(i)
print(s)

