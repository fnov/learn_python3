# 07-1-final-lab-csv

##isbn|title|author|quantity|price
##978-1-43545-500-9|Python Prоgramming for the Absolute Beginner|Michael Dawson|10|18.90
##978-0-59600-372-2|XSLT Cookbook|Sal Mangano|15|34.60
##978-0-32168-056-3|Programming in Python 3|Mark Summerfield|8|27.28
##978-1-44935-573-9|Learning Python|Mark Lutz|21|34.20
##978-0-47178-597-2|Ajax For Dummies|Steve Holzner|32|11.80
##978-1-78439-700-5|Mastering Python Networking|Eric Chou|23|31.49
##978-8-59037-986-7|Programming in Lua|Roberto Ierusalimschy|12|37.10
##978-1-78439-658-9|Machine Learning in Java|Bostjan Kaluza|45|34.99

import csv
import re

def get_books(filename):
    '''Return books in list of lists'''
    data = []
    def cast_value(data):
        if data[3].isdigit():
            data[3] = int(data[3])
            data[4] = float(data[4])
    with open (filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter = '|')
        for row in reader:
            cast_value(row)
            data.append(row)
    data.pop(0)
    return data

def filter_books(books, needle):
    '''Return books in list of lists filtered by needle'''
    data = []
    pattern = re.compile(needle, re.I)
    for book in books:
        if patter.search(book[1]):
            data.append(book)
    return data

@get_totals_with_inc(500, 100)
def get_totals(books):
    ''' '''
    return list(map(lambda b: (b[0], b[3]*b[4]), books))

def get_totals_with_inc(min_order, inc):
    ''' '''
    def decor(fn):
        def wrapper(books):
            totals = fn(books)
            return list(map(lambda b: b if b[1]>=min_order else (b[0], b[1]+inc), totals))
        return wrapper    
    return decor

infile = 'book.csv'
all_books = get_books(infile)
python_books = filter_books(all_books, 'python')
totals = get_totals(python_books)
get_totals_with_inc = get_totals(python_books)



