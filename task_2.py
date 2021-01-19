'''Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

def my_func(**kwargs):
    return kwargs

print(my_func(name=input('Enter Name: '), second_name=input('YEnter Second Name: '), year=input('Enter year of birth: '), city=input('Enter Current city: '), email=input('Enter E-mail: '), phone=input('Enter phone number: ')))