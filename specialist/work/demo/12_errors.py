# demo/errors.py
# 12 exceptions

try:
    print('start')
        f = open('data.txt')
            x = 10/0
                print(x)
                    x = 'a' * 's'
                        Print(x)
except ZeroDivisionError:
    print('dont divise by zero!')
except TypeError:
    print('type error')
except Exception:
    print('shit happens')

    print('finish 1st block')

    ##try:
    ##    txt = input('Type something: ')  
    ##except EOFError:
    ##    print('EOF detected')
    ##except KeyboardInterrupt:
    ##    print('You enterd CTRL+C|Z (windows OMG!). Dont do this')
    ##
    ##print('You type ' + txt)

try:
    print('start')
        f = open('data.txt')
            Print('ololo')
except Exception:
    print('shit happens')
finally: # do this no matter what (we got exception or not)
    f.close()

print('finish 2nd block')


age = int(input('How old are you? '))
try:
    if age > 100:
        raise Exception('you are super star')
        print('start')
except Exception as e:
    print(e)
        
print('finish 3d block')

# 13 raise exceptions from function

def foo():
    print('foo')
    raise Exception('from foo')
    return 1
def bar(x):
    print('bar')
    raise Exception('from bar')
    return x + 10
def baz(b):
    print('baz', b)
    
try:
    a =foo()
    b = bar(a)
    baz(b)
except Exception as e:
    print(e)
    
print('finish 1th block')

# 14 type hints

name: str #expect name to be string
age: int = 25 #expect name to be integer

def add(n1: int, n2: int) -> int: # expect function to return int
    return n1 + n2
    
add(2.5, 3)
name = 10
age = input('...')

############################################

from typing import List, Dict, Tuple # impor typing module

a: List[int] # expect list of integers
b: Dict[str, str] # expect dictionaty of strings
c: List[Tuple[str, int]] # expect list-tuple of str and int
