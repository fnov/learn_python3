# 03-2-wheel-of-fortune
import random

msgs = {
    'enter': 'Type letter or word: ',
    'wrong': 'Wrong! You lose live!',
    'win': 'You won and got THE PRIZE!',
    'lose': 'You lose! Word is: ',
    'end': 'Thanks for game!'
    }
def get_data():
    return ['книга', 'месяц', 'ручка', 'шарик', 'олень', 'носок']
def get_word(data):
    random.shuffle(data)
    return data.pop()

def create_table():
    tbl = ['\u25A0', '\u25A0', '\u25A0', '\u25A0', '\u25A0']
    return ' '.join(tbl)

def update_table(char, word, tbl):
    tbl = tbl.split(' ')
    for i in range(len(word)):
        if char.upper() == word[i].upper():
            tbl[i] = char
    return ' '.join(tbl)

def create_live(num_of_lives):
    return '\u2764' + 'x' + str(num_of_lives)

def is_alive():
    return number_of_lives > 0

def is_word_correct(word, trial):
    return trial.replace(' ', '').upper() == word.upper()
def is_letter_correct(word, letter):
    return letter in word

def get_win_msg(word, msg):
    return ' '.join(word).upper() + '\n' + msg
def get_wrong_msg(msg):
    return msg
def get_lose_msg(word, msg):
    return msg + '\n' + ' '.join(word).upper()

words = get_data()  
current_word = get_word(words)
table = create_table()
show_table = '{} | {}'
# lives = create_live(number_of_lives)
number_of_lives = 3

while is_alive():
    print(show_table.format(table, create_live(number_of_lives)))
    answer = input(msgs['enter'])
    if is_word_correct(current_word, answer):
        s = get_win_msg(current_word, msgs['win'])
        print(s)
        break
    elif is_letter_correct(current_word, answer):
        table = update_table(answer, current_word, table)
        if is_word_correct(current_word, table):
            s = get_win_msg(current_word, msgs['win'])
            print(s)
            break
    else:
        s = get_wrong_msg(msgs['wrong'])
        print(s)
        number_of_lives -= 1

else:     
    s = get_lose_msg(current_word, msgs['lose'])
    print(s)

print(msgs['end'])
