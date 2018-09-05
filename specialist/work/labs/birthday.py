# labs/birthday.py
from random import randrange as rand # random.randrange
from random import choice

def birthday(items=23, iteration = 10000):
    num_month = 12
    num_days = 28
    matches = 0

    for i in range(iteration):
        birthdays = []
        rand_month = 0
        rand_day = 0
        for _ in range(items):
##            rand_month = rand(1, num_month+1)
##            rand_day = rand(1, num_days+1)
##            birthdays.append(f'{rand_day}-{rand_month}')
            birthdays.append( rand(1, 337) )
        # birthdays[rand(1, 366) for _ in range(birthday_to_generate)]    
        
        tmp = set(birthdays)    
        if len(birthdays) != len(tmp):
            matches += 1
    return matches / iteration * 100
    
    
    
    
    
    

