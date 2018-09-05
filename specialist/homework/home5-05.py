#!/usr/bin/python

#Для заданного целого числа N напечатайте все квадраты положительных целых чисел, где квадрат
#меньше или равен N в порядке возрастания.

n = int(input())
array = []
x = 1
sq = lambda n: n**2

while sq(x) <= n:
    array.append(sq(x))
    x += 1
       
print(*array)
