""" Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу: 
(выработка в часах*ставка в час) + премия. Для выполнения расчета для 
конкретных значений необходимо запускать скрипт с параметрами."""
def function():
    while True:
        try:
            x = int(input())
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x

def salary(work_time, hour_salary, prize):
    return work_time*hour_salary+prize
print('Введите отработанное сотрудником время : ')
w_time = function()
print('Введите з/п сотрудника в час  :')
h_salary = function()
print('Введите премию : ')
m_prize = function()
print(f'Заработная плат сотрудника : {salary(w_time, h_salary,m_prize)}')


