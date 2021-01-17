# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()
input_list = input("Введите элементы списка через пробел: ")
input_list = input_list.replace(' ', '')
print(list(input_list))
s = len(input_list)
a = []
i = 0
if (s % 2) == 0:
    while i != s:
        el = input_list[i]
        i = i + 1
        el_2 = input_list[i]
        a.append(el_2)
        a.append(el)
        i = i + 1
else:
    s = s - 1
    while i != s:
        el = input_list[i]
        i = i + 1
        el_2 = input_list[i]
        a.append(el_2)
        a.append(el)
        i = i + 1
    a.append(input_list[s])
print(list(a))