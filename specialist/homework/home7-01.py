#!/usr/bin/python

#Вводится текст одной строкой. Каждое слово разделено пробелом.
#Для каждого слова посчитайте количество данного слова встречающегося перед ним.

lst = [s for s in input().split()]

d= {}
count_lst = []

for i in lst:
    if i not in d:
        d[i] = 0
    else:
        d[i] += 1
    count_lst.append(d[i])

print(*count_lst)
