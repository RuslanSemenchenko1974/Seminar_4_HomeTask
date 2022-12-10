"""Задана натуральная степень k. Сформировать случайным образом список
коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
степени k."""
import random


def function():
    while True:
        try:
            x = int(input())
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


print('Задайте степень числа : ')
k = function()
lst = []
for i in range(k + 1):
    lst.append(random.randint(0, 100))
print(lst)
polynomial = []
data = open('file.txt', 'w')
for el in range(1, k + 1):
    polynomial.append(str(lst[el - 1]))
    polynomial.append('*X^')
    polynomial.append(str(el))
    polynomial.append('+')
polynomial.append(str(lst[k]))
polynomial.append(' = 0')
data.writelines(polynomial)
data.close()
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()
