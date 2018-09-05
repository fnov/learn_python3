# labs/monty-hall.py
import random

choice = None # дверь игрока
gift = None # дверь с подарком
eliminated = None # дверь ведущего
win = 0
trial = counter = 10000

while counter > 0:
    counter -= 1
    choice = 1
    gift = random.randrange(1, 4)
    
    if gift == 2:
        eliminated = 3
    elif gift == 3:
        eliminated = 2
    else:
        eliminated = random.randrange(2, 4)
    
    if eliminated == 2:
        choice = 3
    else:
        choice = 2
    
    if choice == gift:
        win += 1
result = win / trial * 100
out = 'Поменяли выбор и выиграли {}%'.format(result)
print(out)
    
    
    