# labs/books.py
import re
import csv

def get_books(filename):
    '''Return books in list of lists'''
    def cast_value(array):
        if array[3].isdigit():
            array[3] = int(array[3])
            array[4] = float(array[4])
    
    array = []
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            cast_value(row)
            array.append(row)
    array.pop(0)
    return array

def filter_books(books, needle):
    '''Return books in list of lists filtered by needle'''
    array = []
    pattern = re.compile(needle, re.I)
    for book in books:
        if pattern.search(book[1]):
            array.append(book)
    return array
    

def get_totals(books):
    return list(map( lambda b: (b[0], b[3]*b[4]), books))

def get_totals_with_inc(min_order, inc=100):
    def decor(fn):
        def wrapper(books):
            totals = fn(books)
            return list(map(lambda b: b if b[1]>=min_order else (b[0], b[1]+inc), totals))
        return wrapper    
    return decor

@get_totals_with_inc(500, 100)
def get_totals(books):
    return list(map( lambda b: (b[0], b[3]*b[4]), books))

infile = 'books.csv'
all_books = get_books(infile)
python_books = filter_books(all_books, 'python')
totals = get_totals(python_books)
totals_with_inc = get_totals(python_books)




