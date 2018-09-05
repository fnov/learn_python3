#!/usr/bin/python

#Дано целое положительное число N.
#Определите, является ли число N числом Фибоначчи. Если это так, напечатайте порядковую позицию
#этого числа, иначе напечатайте -1.
#Позиции для чисел Фибоначчи считайте от первого числа 1, то есть 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

n = int(input())

def fibo():
    fi = [0, 1]
    i = 0
    j = 1
    while i <= 10:
        z = fi[i] + fi[j]
        fi.append(z)
        i += 1
        j += 1
    return fi
    
fin = fibo()

if n in fin:
    print(fin.index(n))
else:
    print (-1)