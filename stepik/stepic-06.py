#!/usr/bin/python3
"""Напишите программу, которая считывает текст из файла
(в файле может быть больше одной строки)
и выводит самое частое слово в этом тексте и через пробел то,
сколько раз оно встретилось. Если таких слов несколько,
вывести лексикографически первое (можно использовать оператор < для строк).
Слова, написанные в разных регистрах, считаются одинаковыми.
Sample Input:

abc a bCd bC AbC BC BCD bcd ABC

Sample Output:

abc 3"""

with open('dataset_3363_3.txt', 'r', encoding='utf-8') as f_in:
    lst = []
    for line in f_in:
        lst += line.lower().strip().split()

d = {}
for i in set(lst):
    x = lst.count(i)
    d.setdefault(i, x)

max_word_count = max(d.values())
for j in sorted(d):
    if d[j] == max_word_count:
        break
print(j, max_word_count)
