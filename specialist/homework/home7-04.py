#!/usr/bin/python

#На вход подаётся целое число N - количество строк. Далее, подаётся N строк слов, которые
#разделены пробелами.
#Напечатайте слово, которое встречается в строках наибольшее количество раз. Если таких слов
#несколько, то напечатайте то слово, которое стоит раньше других в алфавитном порядке.

N = int(input())

d = {}
for _ in range(N):
    lst = [s for s in input().split()]
    for i in lst:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

max_word_count = max(d.values())
for j in sorted(d):
    if d[j] == max_word_count:
        break
print(j)
