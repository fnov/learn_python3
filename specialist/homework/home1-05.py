#!/usr/bin/python

#N студентов получают K яблок и распределяют их друг другу поровну. Оставшиеся яблоки
#складываются в корзину.
#Сколько яблок имеет каждый студени? Сколько яблок находится в корзине?
#Напишите код, который принимает числа N и K и печатает ответ на два вышезаданных вопроса.

student = int(input())
apple = int(input())
s_apple = apple//student
b_apple = apple%student
mesg = f'Each student have {s_apple} apples, {b_apple} in busket'
print(mesg)
