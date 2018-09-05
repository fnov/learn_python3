#!/usr/bin/python

#Дана последовательность неотрицательных целых чисел, где каждое число записывается в отдельной
#строке. Последовательность заканчивается на 0.
#Напечатайте длину самого широкого фрагмента последовательности, где все элементы равны друг
#другу.

array = []
n = 1

while n !=0 :
    n = int(input())
    array.append(n)

lenth = len(array)
match = []

y = 1
z = 1
for x in array:
    if y == lenth:
        break
    elif x == array[y]:
        z +=1
    else:
        match.append(z)
        z =1
    y += 1

match.sort()
print(match[-1])
