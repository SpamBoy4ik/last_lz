from math import sqrt

volume_truncated_pyramid = lambda s1, s2, height: 1/3 * height * (s1 + sqrt(s1 * s2) + s2) # вычисление объема

def main():
    print('Вычисление объема усеченной пирамиды.')
    s1 = float(input('Площадь верхнего основания: '))
    s2 = float(input('Площадь нижнего основания: '))
    height = float(input('Высота: '))
    print(volume_truncated_pyramid(s1, s2, height))


if __name__ == '__main__':
    main()
    