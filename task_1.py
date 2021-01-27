'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

with open("my_file.txt", 'w', encoding='utf-8') as my_file:
    while True:
        text = input()
        m = ''.join(text)
        if not text:
            break
        else:
            my_file.write(f"{m}\n")