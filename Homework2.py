# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = str(input('Введите любое вещественное число: '))
# sum = 0
# number1 = number.replace('.','')
# for i in range(len(number1)):
#     sum += int(number1[i])
# print(f'Сумма цифр числа {number} равна {sum}')

# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран,
# а так же сумму элементов списка.

# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# n = int(input('Введите n: '))
# sum = 0
# p = 0
# print('[', end='')
# for i in range(1, n):
#     p = (1 + 1 / i) ** i
#     sum += p
#     print(round(p, 2), end=', ')
# print(f'{round((1 + 1 / n) ** n, 2)}]')
# print(f'Сумма элементов списка равна {round(sum + (1 + 1 / n) ** n, 2)}')

# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ
# БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для
# и получения случайного int

# import random
# list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(list)
# temp = 0
# for i in range(len(list)):
#     a = random.randrange(i, len(list))
#     if a != i:
#         temp = list[i]
#         list[i] = list[a]
#         list[a] = temp
# print(list)
