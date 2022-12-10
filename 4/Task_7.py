""" Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен  создаваться объект-
генератор.
Функция должна вызываться следующим образом: for el in fact(n). Функция
отвечает за получение факториала числа, а в цикле необходимо выводить только
первые n чисел, начиная с 1! и до n!."""

#         ***Условие не совсем понятно***

def fact(namber):
    for i in range(1, namber + 1):
       yield i

n = int(input('Введите число : '))
prom=1
for el in fact(n):
    prom*=el
    print(el)
print('Факториал : ',prom)

"""  # Второй вариант
def fact(namber):
    prom = 1
    for i in range(1, namber + 1):
        prom = prom * i
    yield prom


n = int(input('Введите число : '))
for el in fact(n):
    print(el)
"""