"""Задайте последовательность чисел. Напишите программу, которая выведет
список неповторяющихся элементов исходной последовательности."""

user_str = input('Ведите числа через пробел : ')
user_list = user_str.split()
namber_list=[]
for i in user_list:
    try:
        x = int(i)
    except ValueError:
        x = 0
    else:
        namber_list.append(x)
print(set(namber_list))
