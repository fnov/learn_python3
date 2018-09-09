#!/usr/bin/python

#На вход подаётся строка из целых чисел разделённых пробелами.
#Напечатайте числа, которые больше, чем число слева от них.
#Сформировать список можно так: lst = [int(s) for s in input().split()]

lst = [int(s) for s in input().split()]
lenth = len(lst)
bolshe = []

y = 1
for x in lst:
    if y == lenth:
        break
    elif x < lst[y]:
        bolshe.append(lst[y])
    y += 1
    
print(*bolshe)

