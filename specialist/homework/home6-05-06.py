#!/usr/bin/python

#На вход подаются две строки целых чисел.
#Напечатайте количество чисел из первой строки, которые встречаются во второй строке.
#Сформировать список можно так: lst = [int(s) for s in input().split()]

lst1 = [int(s) for s in input().split()]
lst2 = [int(s) for s in input().split()]

#count = 0
#for i in lst1:
#    if i in lst2:
#        count += 1
lstx = [s for s in lst1 if s in lst2]
count = len(lstx)
    
print(count)
print(*lstx)
