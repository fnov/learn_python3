# 04-work-with-files

def read_file(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        words = f.read().lower()
        lst = words.split(' ')
        for i, in lst:
            
    
    return lst

file = 'data.txt'

print(read_file(file))
        
        
        
    