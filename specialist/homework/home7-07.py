#!/usr/bin/python

#На вход подаётся целое число N - количество строк подаваемых на вход.
#Далее, подаются N строк из слов. Если слов в строке несколько, они разделяются пробелом.
#Для каждого слова напечатайте его количество. Список слов выведите по частоте.
#Пример ввода
#9
#hi
#hi
#what is your name
#my name is bond
#james bond
#my name is damme
#van damme
#claude van damme
#jean claude van damme
#Пример вывода
#damme 4
#is 3
#name 3
#van 3
#bond 2
#claude 2
#hi 2
#my 2
#james 1
#jean 1
#what 1
#your 1

N = int(input())

d = {}
for _ in range(N):
    lst = [s for s in input().split()]
    for word in lst:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1

sorted_d = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
for k, v in sorted_d:
    print(k, v)
