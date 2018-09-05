# 03-wheel-of-fortune

#word = ['viper', 'taker', 'brown', 'pride']
live = 3
word = 'viper'
un_char0 = un_char1 = un_char2 = un_char3 = un_char4 = '\u25A0'

while live > 0:
    print(f'{un_char0} {un_char1} {un_char2} {un_char3} {un_char4}', '|', live, '\u2764')
    user_input = input('Назовите букву или слово: ')
    if len(user_input) == 5:
        if user_input != word:
            print('You lose. Word is: ', word)
            break
        else:
            print('Вы выиграли! Приз в студию!')
            break
    elif user_input == word[0]:
        un_char0 == word[0]
    elif user_input == word[1]:
        un_char1 == word[1]        
    elif user_input == word[2]:
        un_char2 == word[2]
    elif user_input == word[3]:
        un_char3 == word[3]
    elif user_input == word[4]:
        un_char4 == word[4]
    else:
        print('Wrong! You lose life!')
        live -= 1
            
print('Thanks for game!')


    



