#!/usr/bin/python3
"""Имеется файл с данными по успеваемости абитуриентов.
Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает файл с подобной структурой
и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке,
соответствующей этому абитуриенту.
Также в конце файла, на отдельной строке,
через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам:
Sample Input:

Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667"""

"""Для тех, кто хочет сократить свой код :) написал небольшое руководство по [list comprehension]
на основе примера на stackoverflow.com
# http://stackoverflow.com/questions/16632124/python-emulate-sum-using-list-comprehension
я немного изменил этот пример, чтобы лучше объяснить работу [list comprehension]
и вам было проще понять, как применить этот подход к решению задания

допустим, у нас есть список фруктов, где зафиксированы самые низкие и высокие цены на эти фрукты
т.е. по сути это список списков :)"""
lst = [["apple", 55, 62], ["orange", 60, 74], ["pineapple", 140, 180], ["lemon", 80, 84]]

# выведем этот список для нагляности на экран, используя [list comprehension]
[print(el) for el in lst]
# ['apple', 55, 62]
# ['orange', 60, 74]
# ['pineapple', 140, 180]
# ['lemon', 80, 84]

# если мы хотим подсчитать среднюю цену на каждый из фруктов, то напишем что-то вроде
sumMiddle = 0
for el in lst:
    sumMiddle = (el[1] + el[2]) / 2
    print(sumMiddle)

# или можно сделать это одной строкой
[print((priceLow + priceHigh) / 2) for fruit, priceLow, priceHigh in lst]
"""представьте, что наш список списков - это таблица из трёх столбцов
и мы можем обращаться к столбцам, просто озаглавив их fruit, priceLow, priceHigh
в цикле for, почти как перебор элементов словаря for key, value in d.items() :)

поэтому, когда вы захотите прикинуть, сколько же, от и до, в среднем может стоить
ваша фруктовая корзина, нужно будет посчитать среднее по каждой колонке
вы можете сделать это примерно так"""
sumLow, sumHigh = 0, 0
for el in lst:
    sumLow += el[1]
    sumHigh += el[2]
sumLow /= len(lst)
sumHigh /= len(lst)
print(sumLow, sumHigh)

# или применить кунг-фу списковых выражений и обойтись парой строк :)
print(sum([priceLow for fruit, priceLow, priceHigh in lst]) / len(lst))
print(sum([priceHigh for fruit, priceLow, priceHigh in lst]) / len(lst))

# а где два принта, там и один :)
print(sum([priceLow for fruit, priceLow, priceHigh in lst]) / len(lst), sum([priceHigh for fruit, priceLow, priceHigh in lst]) / len(lst))

# надеюсь, вам было понятно и интересно
# желаю успехов в учёбе!!!

with open('dataset_3363_4.txt', 'r', encoding='utf-8') as f_in:
    lst = []
    for line in f_in:
        lst.append(line.strip().split(';'))

[print((int(mat) + int(fiz) + int(rus)) / 3) for name, mat, fiz, rus in lst]
m = sum([int(mat) for name, mat, fiz, rus in lst]) / len(lst)
f = sum([int(fiz) for name, mat, fiz, rus in lst]) / len(lst)
r = sum([int(rus) for name, mat, fiz, rus in lst]) / len(lst)
print(m, f, r)
