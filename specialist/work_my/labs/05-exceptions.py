# 05-exceptions

def read_file(fname):
        f = open(fname, 'r', encoding='utf-8')
        try:
            return read_data(f)
        finally:
            f.close()

def read_data(file):
    line = file.readline() # read only first string
    number_of_values = int(line) # ValueError
    data = []
    for i in range(number_of_values):
        line = file.readline()
        value = int(line) # ValueError
        data.append(value)
    line = file.readline()
    if line != '':
        raise RuntimeError('лишние данные в конце файла')
    return data
    
done = False
while not done: 
    try:
        name = input('Type filename to work with: ')
        data = read_file(name)
        print(data)
        done = True
    except IOError:
        print('file does not exist')
    except ValueError:
        print('wrong file content')
    except RuntimeError as error:
        print(error)
    