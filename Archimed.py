# держится при F Архимеда >= P (веса)

archimedes_force = lambda mass, volume, density: mass * volume * density # вычисление силы Архимеда

def check_buoyancy_water(mass, volume, density): # проверка на плавучесть
    if archimedes_force(mass, volume, density) < mass * 9.81:
        return False
    return True


def main():
    print('Проверка тела на плавучесть.')
    m = float(input('Введите массу тела (кг): '))
    v = float(input('Введите объем погруженной части тела (куб. м): '))
    p = float(input('Введите плотность тела (кг/м3): '))
    if check_buoyancy_water(m, v, p):
        print('Тело не утонет.')
    else:
        print('Тело утонет.')


if __name__ == '__main__':
    main()
