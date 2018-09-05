# demo/funcs.py
def add(a, b):
    return a+b
    
def area_of_disk(radius):
    '''Help on user-defined function area_of_disk:
        
       area_of_disk(radius)
           Return the area of disk with current radius
    '''
    return 3.14 * radius ** 2

def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)

def __puts(*args, ln='\n'): # list(1,2,3)
    for i in args:
        print(i, end=ln)

##for i in range(2, 8):
##    print('Квадрат числа', i, '=', i**2)
##for i in range(3, 5):
##    print(Куб числа', i, '=', i**3)
  