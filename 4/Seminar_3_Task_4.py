""" Программа принимает действительное положительное число x и целое
отрицательное число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y). При решении
задания необходимо обойтись без встроенной функции возведения числа
в степень."""
# Исправленное задание

def function_inter():
    while True:
        try:
            x = float(input())
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


def function_inter2():
    while True:
        try:
            x = int(input())
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            if x<0:
                return x
            else:
                print('Введите отрицательное число')


def my_func(x, y):
    temp = 1
    for i in range(abs(y)):
        if y < 0:
            temp /= x
        elif y == 0:
            temp = 1
        else:
            temp *= x
    print(f'{x} в степени {y} = {temp}')


print('Введите число : ')
us_namber = function_inter()
print('Введите степень числа : ')
us_degree = function_inter2()
my_func(x=us_namber, y=us_degree)