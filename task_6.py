'''
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
'''
n = input()

def int_func():
    t = n.lower()
    l = k = 0
    m = int(len(n))
    while m != 0:
        # print(ord(n[m-1]))
        if (ord(n[m - 1]) - 97) <= 25:
            l = ord(t[m - 1]) + l - 97
            k = ord(n[m - 1]) + k - 97
            # print(l)
            # print(k)
            # print(n[m-1])
            m = m - 1
        elif (ord(n[m - 1]) - 97) >= 25:
            print('Присутствует кириллица')
            k = k - 1
            break
        else:
            k = k - 1
            m = m - 1
    if k == l:
        z = n.title()
    else:
        z='Не правильное слово'

    return z


print(int_func())

'''


'''
