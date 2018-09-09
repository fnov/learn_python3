#!/usr/bin/python

#На вход подаётся целое число N - количество записей в словаре. Далее подаются N пар: фамилия
#кандидата в президенты и число проголосовавших.
#Задача посчитать и вывести фамилии кандидатов с общим числом, которое они набрали. Фамилии
#вывести в алфавитном порядке.
#Пример ввода
#5
#Smith 5
#Smith 1
#Dow 9
#Dow 8
#Smith10
#Пример вывода
#Dow 17
#Smith 16

N = int(input())

d = {}
for _ in range(N):
    l = input().split()
    name = l[0]
    proc = int(l[1])
    if name not in d.keys():
        d[name] = proc
    else:
        d[name] += proc
        
for i in sorted(d):
    print(i, d[i])
