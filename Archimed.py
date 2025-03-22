# держится при F Архимеда >= P (веса)

archimedes_force = lambda mass, volume, density: mass * volume * density # вычисление силы Архимеда

def check_buoyancy_water(mass, volume, density): # проверка на плавучесть
    if archimedes_force(mass, volume, density) < mass * 9.81:
        return False
    return True

def check_positive(*numbers): # проверка числа на положительность
    for number in numbers:
        if number <= 0:
            return False
    return True


def main():
    print('Проверка тела на плавучесть.')
    m = float(input('Введите массу тела (кг): '))
    v = float(input('Введите объем погруженной части тела (куб. м): '))
    p = float(input('Введите плотность тела (кг/м3): '))
    if check_positive(m, v, p):
        if check_buoyancy_water(m, v, p):
            print('Тело не утонет.')
        else:
            print('Тело утонет.')
    else:
        print('Масса, объем и плотность должны быть положительными.')
        

if __name__ == '__main__':
    main()
