from math import sqrt

volume_truncated_pyramid = lambda square1, square2, height: 1/3 * height * (square1 + sqrt(square1 * square2) + square2) # вычисление объема

def check_positive(*numbers): # проверка числа на положительность
    for number in numbers:
        if number <= 0:
            return False
    return True


def main():
    print('Вычисление объема усеченной пирамиды.')
    s1 = float(input('Площадь верхнего основания: '))
    s2 = float(input('Площадь нижнего основания: '))
    height = float(input('Высота: '))
    if check_positive(s1, s2, height):
        print(f'Объем усеченной пирамиды: {volume_truncated_pyramid(s1, s2, height)}')
    else:
        print('Площади и высота должны быть положительными.')
    


if __name__ == '__main__':
    main()
    