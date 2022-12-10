"""Задайте натуральное число N. Напишите программу, которая составит список
простых множителей числа N."""
def function():
    while True:
        try:
            x = int(input())
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x

print("Введите число")
n = function()
my_lst = []
while n != 1:
    for i in range(2, n+1):
        if n % i == 0:
            n = int(n / i)
            my_lst.append(i)
            break
print(my_lst)
