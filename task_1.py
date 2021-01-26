'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

my_file = open("some.txt", 'w')
while True:
    text = input()
    m = ''.join(text)
    if not text:
        break
    else:
        my_file.write(f"{m}\n")