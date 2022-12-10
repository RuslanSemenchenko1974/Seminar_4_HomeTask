""" Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль."""
# Исправленное задание

def function_inter():
    while True:
        try:
            x = float(input())
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x
def division(n1,n2):
    return namber_1 / namber_2

print('Введите делимое  : ')
namber_1 = function_inter()
namber_2 = 0
while namber_2 == 0:
    print('Введите делитель  : ')
    namber_2 = function_inter()
    if namber_2 == 0:
        print('Делить на ноль нельзя!')
print(
    f'Результат деления {namber_1} на {namber_2} равен : '
    f'{division(namber_1, namber_2)}')