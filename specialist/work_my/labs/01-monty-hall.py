# 04-monty-hall

import random
choice = 0 # or None
gift = None
opened = None
win = 0
trial = counter= 10000

while counter > 0:
    counter -= 1
    choise = 1
    gift = random.randrange(1, 4)
    if gift == 2:
        opened = 3
    elif gift == 3:
        opened = 2
    else:
        opened = random.randrange(2, 4)
    
    if opened == 2:
        choice = 3
    else:
        choice = 2
    
    if choice == gift:
        win +=1
        
result = win/trial * 100
out = 'Change door and win {}%'.format(result)
print(out)
    
    
    
    
    
    
    
    