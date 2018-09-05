#!/usr/bin/python

#На вход подаётся строка из целых чисел разделённых пробелами.
#Напечатайте числа, поменяв пары чисел местами,
#то есть первое со вторым, третье с четвёртым и т.д.
#Сформировать список можно так: lst = [int(s) for s inut().split()]

lst = [int(s) for s in input().split()]
len_lst = len(lst)
range_lst = range(len_lst)
new_lst = []

for x in range_lst[::2]:
    y = x + 1
    if y < len_lst:
        tmp_lst = [lst[x],lst[y]]
        tmp_lst.reverse()
        new_lst.extend(tmp_lst)
    elif x < len_lst:
        new_lst.append(lst[x])
    else:
        break
    
print(*new_lst)


