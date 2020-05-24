#!/usr/bin/python3
"""Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
удаляет из него все нечётные значения, а чётные нацело делит на два.
Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4] """


def modify_list(lst):
    lst[:] = [i // 2 for i in lst if not i % 2]


numbers = [1, 2, 3, 4, 5, 6]
modify_list(numbers)
print(*numbers)
