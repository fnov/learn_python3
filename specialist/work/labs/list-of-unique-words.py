# labs/list-of-unique-words.py

def read_file(filename):
    '''Return list of unique words from given filename'''
    
    def clean(s):
        result = ''
        for char in s:
            if char.isalpha():
                result += char.lower()
        return result
    
    with open(filename, 'r', encoding='utf-8') as f:
        unique_words = set()
        for line in f:
            words = set(line.split(' ')) 
            if len(words) == 0:
                continue
            for word in words:
                cleaned = clean(word)
                if cleaned != '':
                    unique_words.add(cleaned)
        return list(unique_words)        
    

def save_file(filename, words):
    '''Save unique words from given list to filename'''
    words = list(words)
    words.sort()
    count = 'Всего уникальных слов: {}'.format(len(words))
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(count + '\n')
        f.write('='*20 + '\n')
        for word in words:
            f.write(word + '\n')


input_file = 'data.txt'
output_file = 'words.txt'

words = read_file(input_file)
save_file(output_file, words)



