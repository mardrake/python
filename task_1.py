try:
    n = input('Введите еще числа, через пробел или введите q: ').split()
    for i, item in enumerate(n):
        a.append(int(item))
    print('Сумма: ', sum(a))
except ValueError:
    print('Сумма: ', sum(a))