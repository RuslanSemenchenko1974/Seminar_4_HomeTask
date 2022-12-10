"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""
# Исправленное задание


def function_inter():
    while True:
        try:
            x = float(input())
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


def my_func(a1, a2, a3):
    my_list = [a1, a2, a3]
    my_list.sort()
    print(my_list[1]+my_list[2])


us_nambers = []
for i in range(3):
    print(f'Введите {i + 1} число : ')
    temp = function_inter()
    us_nambers.append(temp)
my_func(us_nambers[0], us_nambers[1], us_nambers[2])