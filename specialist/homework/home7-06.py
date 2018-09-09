#!/usr/bin/python

#На вход подаётся целое число N - количество строк подаваемых на вход. Далее, подаются N строк формате "страна город город ...". Далее, на вход подаётся целое число М - количество следующих
#подаваемых строк. Далее, M городов.
#Для каждого переданного города напечатайте страну, в которой он находится.
#Пример ввода
#2
#USA Boston Pittsburgh Washington Seattle
#UK London Edinburgh Cardiff Belfast
#3
#Cardiff
#Seattle
#London
#Пример вывода
#UK
#USA
#UK

N = int(input())

d = {}
for _ in range(N):
    lst = [s for s in input().split()]
    d[lst[0]] = lst[1:]

M = int(input())
lst_r = []
for _ in range(M):
    city = input()
    for i in d.keys():
        if city in d[i]:
            lst_r.append(i)

print(*lst_r, sep='\n')
