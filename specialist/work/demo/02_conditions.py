# demo/conditions.py
import random

while True:
    n1 = random.randrange(1, 11)
    n2 = random.randrange(1, 11)
    answer = input(f'Сколько будет {n1} + {n2} = ')
    
    if answer == '0':
       break
    
    test = answer.replace('.', '', 1)

    if not test.isdigit():
        print('Введите число цифрами!')
        continue
    
    if answer == test:
        answer = int(answer)
    else:
        answer = float(answer)
    
    if n1+n2 == answer:
        print('Правильно!')
    else:
        print('Не правильно!')

