#4. Задача: Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input('Введите номер четверти, число от 1 до 4: '))

if(quarter_number == 1):
    print('возможные координаты по оси x: (1, ∞)')
    print('возможные координаты по оси y: (1, ∞)')
elif(quarter_number == 2):
    print('возможные координаты по оси x: (-1, -∞)')
    print('возможные координаты по оси y: (1, ∞)')
elif(quarter_number == 3):
    print('возможные координаты по оси x: (-1, -∞)')
    print('возможные координаты по оси y: (-1, -∞)')
elif(quarter_number == 4):
    print('возможные координаты по оси x: (1, ∞)')
    print('возможные координаты по оси y: (-1, -∞)')
else:
    print('число введено не верно')