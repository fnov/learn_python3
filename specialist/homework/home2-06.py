#!/usr/bin/python

#Дано вещественное положительное число.
#Напечатайте первую цифру справа после точки.

number = input()
for i in range(len(number)):
    if number[i] == '.':
        i = i+1
        break
print(number[i])