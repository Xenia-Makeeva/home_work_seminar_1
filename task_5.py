#5. Задача: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math


a_1 = int(input('Введите координату точки а по оси x: '))
a_2 = int(input('Введите координату точки а по оси y: '))
b_1 = int(input('Введите координату точки b по оси x: '))
b_2 = int(input('Введите координату точки b по оси y: '))

distance = round(math.sqrt((b_1 - a_1) ** 2 + (b_2 - a_2) ** 2),2)
print(distance)