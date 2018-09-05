# demo/files.py
import os
import sys

print ('Script name ', sys.argv[0] ) # $0
print ('First argument ', sys.argv[1] ) # $1 etc

os.getcwd() # pwd, use help os
r'c:\users\kolya' # not format, raw string
os.listdir() # ls

sys.path

# 10 work with fs
#open('data.txt', 'r') # read file data.txt
#open('data.txt', 'r+') # read and overwrite file data.txt FROM FIRST SYMBOL
#open('data.txt', 'w') # only write file data.txt (>)
#open('data.txt', 'w+') # only write file data.txt
#open('data.txt', 'a') # write file data.txt (>>)
#open('data.txt', 'a+') # read and write file data.txt
#f = open('data.txt', 'r', encoding='utf-8')
#f.close() # close file after work is done
#lst = []
import csv

with open('data.txt', 'r', encoding='utf-8') as f: # = f = open('data.txt', 'r', encoding='utf-8') (auto close)
    #print(f.read(5)) # 5 first symbols of file
    #print(f.read()) # whole file
    #print(f.readline()) # strings of file (first string if no argument)
    #s = f.readline()
    #while s:
        #lst.append(s)
        #s = f.readline()
   #lst = f.readlines() # strings to list
   for line in f: # f.readlines too
       print(line)
       
with open('data.txt', 'a', encoding='utf-8') as f:
    #f.write('\nLine seven') # write to file
    #f.tell() # where is my cursor
    #f.seek() # move cursor from beginning of file
    print(f.closed) # file closed (True) or no (False), use without
    print(f.mode) # mode of work with file (r w a)
    print(f.name) # name of file
    print(f.encoding) # encoding of file

with open('users.csv', 'r', encoding='utf-8') as f:
    #reader = csv.reader(f, delimiter = ',')
    writer = csv.writer(f, delimiter = ',')
    writer.writerow(['mike', 'bazinsky', 33,'1-800-call-merlini'])
    #for row in reader:
        #print(row)
     

