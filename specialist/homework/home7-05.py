#!/usr/bin/python

#На вход подаётся целое число N - количество файлов в файловой системе.
#Далее, подаются N строк в формате "имя файла" и допустимые операции разделённые пробелами.
#Допустимые операции следующие: W - write, R - read, X - execute.
#Далее, подаётся целое число М - количество операций с файлами.
#Далее, подаётся М строк в формате "операция имя файла".
#Напечатайте "OK", если такая операция с файлом допустима и "Denied", если нет.
#Пример ввода
#4
#notepad.exe R X
#access.log W R
#logo.gif R
#httpd.conf X W R
#5
#read logo.gif
#write notepad.exe
#execute logo.gif
#read access.log
#write access.log
#Пример вывода
#OK
#Denied
#Denied
#OK
#OK

def cut_right(name):
    dd = {'read': 'R', 'write': 'W', 'execute': 'X'}
    return dd[name]

N = int(input())

d = {}
for _ in range(N):
    lst = [s for s in input().split()]
    d[lst[0]] = lst[1:]

M = int(input())
lst_r = []
for _ in range(M):
    lst = [s for s in input().split()]
    i = lst[0]
    j = lst[1]
    I = cut_right(i)
    if I in d[j]:
        lst_r.append('OK')
    else:
        lst_r.append('Denied')

print(*lst_r, sep='\n')