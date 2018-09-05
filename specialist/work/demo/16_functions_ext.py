# 16 functions extended
def power_of(start_n, end_n, exponent):
    for i in range(start_n, end_n+1):
        yield i, i ** exponent # return, but not exit of function, stop and wait for run code
        print('anything') # not run until all yield is done
        
for i, result in power_of(4, 8, 2):
    print('square of number', i, '=', result)
    
import os
for fname in os.scandir('.'):
    print(fname.name) # ls

# array of strings to array of int
array = ['1', '2', '3', '4', '5', '6', '7']
array_of_ints = []
for item in array:
    array_of_ints.append(int(item))
    
# another way
array_of_ints = map(int, array)
array_of_ints = list(array_of_ints)

by_ten = map(lambda i: i*10, array_of_ints) # list of numbers * 10
by_ten = list(by_ten)

# array to array of number > 5
array = [9, 7, 3, 4, 5, 2, 8]
new = filter(lambda n: n>5, array) # filter expect bool (True or False)
new_list = list(new)

from functools import reduce # what is reduce?
array = [9, 7, 3, 4, 5, 2, 8]
sum_all = reduce(lambda a,b: a+b, array) # reduce return value, has always 2 arguments# 16 decorators

# 17 decorators

def hello():
    return 'hello'
def add_underscores(fn):
    return lambda: '_' + fn() + '_'

hello = add_underscores(hello)

# equal to
def add_underscores(fn):
    return lambda: '_' + fn() + '_'

@add_underscores # decorate function hello (@ is decorator)
def hello():
    return 'hello'

######################

def add_symbols(left, right):
    def decor(fn):
        return lambda name: left + fn(name) + right
    return decor

@add_symbols('-', '*')
def hello(name):
    return 'hello ' + name

# 18 memorization

def square(n):
    print('here')
    return n**2

#{4:16, 2:4, 3:9}

def memorize(fn):
    memo = {}
    def _(n):
        if m not in memo:
            memo[n] = fn(n)
        return memo[n]
    return _
    
square = memorize(square)

# same
import functools

@functools.lru_cache(maxsize=32)
def square(n):
    print('here')
    return n**2


# 19
# function
#Принимает 3 числа целых положительных
#Возвращает сумму квадратов двух наибольших из них

square = lambda n: n*n
sum_of_squares = lambda a,b: square(a)+square(b)
larger = lambda a,b: a if a>b else b


def sum_of(a, b, c):
    if a == larger(a,b):
        return sum_of_squares(a, larger(b, c))
    return sum_of_squares(b, larger(a, c))

######### second version

def sum_of(*nums):
    nums = list(nums)
    nums.sort()
    #nums.pop(0)
    return sum_of_squares(nums[0], nums[1])

sum_of(5, 3, 7)


