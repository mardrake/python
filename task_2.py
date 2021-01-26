'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''
stroka = 0
t = 0
with open("some.txt", 'r', encoding='utf8') as my_file:
    for line in my_file:
        stroka = stroka + 1
        print(stroka, ':строка!', len(line) - 1, ':слов!')

print('Количество строк в файле = ', stroka)
