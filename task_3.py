#3. Задача: Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

coordinate_x = int(input('Введите значение по оси x, отличное от 0: '))
coordinate_y = int(input('Введите значение по оси y, отличное от 0: '))
if(coordinate_x > 0 and coordinate_y > 0):
    print('номер четверти: 1')
elif(coordinate_x < 0 and coordinate_y > 0):
    print('номер четверти: 2')
elif(coordinate_x < 0 and coordinate_y < 0):
    print('номер четверти: 3')
elif(coordinate_x > 0 and coordinate_y < 0):
    print('номер четверти: 4')
else:
    print('число введено не верно')