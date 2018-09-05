#!/usr/bin/python

#Дано целое положительное число N.
#Напечатайте число Фибоначчи, которое находится в позиции числа N.
#Позиции для чисел Фибоначчи считайте от первого числа 1, то есть 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

n = int(input())

def fibo(n):
    i = 0
    j = 1
    fi = [0, 1]
    while j < n:
        z = fi[i] + fi[j]
        fi.append(z)
        i += 1
        j += 1
    return fi
    
fin = fibo(n)
print(fin[n])
