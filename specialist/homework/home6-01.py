#!/usr/bin/python

#На вход подаётся строка из целых чисел разделённых пробелами.
#Напечатайте все нечётные числа из введённой строки.
#Сформировать список можно так: lst = [int(s) for s in input().split()]

lst = [int(s) for s in input().split()]

nechet = [x for x in lst if x%2 != 0]

print(*nechet)
