import Archimed, pyramid


choice = int(input('Проверить тело на плавучесть(0) или найть объем усеченной пирамиды(1): '))
if choice == 0: Archimed.main()
elif choice == 1: pyramid.main()
else: print('Выборы был 0 или 1.')
