# labs/errors.py
def read_file(filename):
    f = open(filename, 'r')
    try:
        return read_data(f)
    finally:
        f.close()

def read_data(file):
    line = file.readline()
    number_of_values = int(line) # ValueError
    data = []
    for i in range(number_of_values):
        line = file.readline()
        value = int(line) # ValueError
        data.append(value)
    line = file.readline()
    if line != '':
        raise RuntimeError('Лишние данные в конце файла')
    return data    

done = False
while not done:
    try:
        name = input('имя файла: ')
        data = read_file(name)
        print(data)
        done = True
    except IOError:
        print('Ошибка: файл не найден!')
    except ValueError:
        print('Ошибка: не то содержимое файла!')
    except RuntimeError as error:
        print('Ошибка:', error)
