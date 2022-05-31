from sys import argv

def zp_func():
    try:
        time, rate, bonus = map (float, argv[1:])
        print(f'Зарплата - {time, rate, bonus}')
    except ValueError:
        print('Введите все три значения')

