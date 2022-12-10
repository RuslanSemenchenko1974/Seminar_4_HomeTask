""" Реализовать формирование списка, используя функцию range() и возможности
генератора. В список должны войти четные числа от 100 до 1000
(включая границы). Необходимо получить результат вычисления произведения всех
элементов списка."""
from functools import reduce
generator = (i for i in range(100, 1001) if i % 2 == 0)
my_lst = []
for el in generator:
    my_lst.append(el)
print(my_lst)
mult_all = reduce(lambda x, y: x * y, my_lst)
print(mult_all)
