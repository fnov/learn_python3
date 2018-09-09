#!/usr/bin/python

#На вход подаётся строка из целых уникальных чисел разделённых пробелами.
#Напечатайте числа, поменяв минимальное и максимальное числа местами.
#Сформировать список можно так: lst = [int(s) for s in input().split()]

def ch_lst(val, ind, data):
    data.remove(val)
    data.insert(ind, val)
    return data

lst = [int(s) for s in input().split()]

lstn = lst[:]
min_lst = min(lstn)
max_lst = max(lstn)
x = lstn.index(min_lst)
y = lstn.index(max_lst)

ch_lst(min_lst, y, lstn)
ch_lst(max_lst, x, lstn)

print(*lstn)
