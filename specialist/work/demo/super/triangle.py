# demo/triangle.py
def draw_triangle(lines=5, symbol='*'):
    for line_number in range(1, lines+1):
        print(symbol * line_number)

if __name__ == '__main__':
    draw_triangle()
else:
    print('Я модуль:', __name__)