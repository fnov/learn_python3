# 08 functions

def wrestler(name):
    print('Best wrewtler is', name)
    
def draw_triangle(lines, symbol='$'):
    for line_number in range(1, lines+1):
        print(symbol * line_number)

if __name__ == '__main__': # do function only we not module
    draw_triangle(10)
        
def add(a, b):
    # Usage and help(function) below
    '''Calculate numbers a + b 
    '''
    return a+b

def puts(*args): #list(1,2,3...)
    for i in args:
        print(i, end=' ')
