'''
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
'''
n = input()
t = ''.join(n).split()
n = ' '.join(t)


def int_func():
    m = n.lower().capitalize()

    return m


print(int_func())
