# 04-1-work-with-files

def read_file(fname):
    '''Return list of unique words from given filename'''
    
    def clean(word):
        result = ''
        for char in word:
            if char.isalpha():
                result += char.lower()
        return result
    
    with open(fname, 'r', encoding='utf-8') as f:
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
    
def save_file(fname, words):
    '''Save unique words from given file to another filename'''
    words.sort()
    count = 'всего уникальных слов: {}'.format(len(words))
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(count + '\n')
        f.write('='*20 + '\n')
        for word in words:
            f.write(word + '\n')

input_file = 'data.txt'
output_file = 'words.txt'

words = read_file(input_file)
save_file(output_file, words)