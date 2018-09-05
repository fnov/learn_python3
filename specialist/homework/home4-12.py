#!/usr/bin/python

#Даны два целых числа. Первое - в диапазоне от 1 до 12 календарный месяц. Второе - в диапазоне от
#1 до 31 день месяца заданного первым числом.
#Напечатайте дату для следующего дня от заданного в формате день-месяц-год для текущего года.

m = int(input())
d = int(input())

def ndays(month):
    m28 = (2,)
    m30 = (4, 6, 9, 11)
    if month in m30:
        o = 30
    elif month in m28:
        o = 28
    else:
        o = 31
    return o
   
days = ndays(m)

if d == days:
    nd = 1
    if m >= 12:
        m = 1
    else:
        m += 1
else:
    nd = d + 1

print(f'{nd}-{m}-2018')