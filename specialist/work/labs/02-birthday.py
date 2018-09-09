 # 02 birthday
 
from random import randrange

def bdays_check(mans = 23, iteration = 10000):
    match = 0
    for i in range(iteration):
        bdays = []
        for _ in range(mans):
            bdays.append( randrange(1, 366) )
        tmp = set(bdays)
        if len(bdays) != len(tmp):
            match += 1
            
    result = match/iteration * 100
    out = '{}%'.format(result)
    return(out)

