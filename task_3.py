'''
 Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''

arg_1 = int(input('Enter first number: '))
arg_2 = int(input('Enter first second: '))
arg_3 = int(input('Enter first third: '))


def my_func(arg_1, arg_2, arg_3):
    m = min(arg_1, arg_2, arg_3)
    if m == arg_1:
        arg_1 = 0
    elif m == arg_2:
        arg_2 = 0
    else:
        arg_3 == 0

    return arg_1+arg_2+arg_3


print(my_func(arg_1, arg_2, arg_3))
