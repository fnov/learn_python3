#!/usr/bin/python

#Даны два целых числа X и Y. Бегун в первый тренировачный день пробежал X километров. Всего
#бегун должен набегать Y километров. Каждый день бегун пробегает дистанцию на 10% длинее
#дистанции предыдущего дня.
#Напечатайте количество дней, которое понадобится бегуну, чтобы пробежать общее число
#километров (число Y).

rkm = int(input())
ekm = int(input())
days = 1

while ekm >= rkm:
    rkm *= 1.1
    days += 1
       
print(days)

