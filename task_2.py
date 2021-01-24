'''
Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
'''
n = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
a = 0
new_list = [n[a] for a in range(1, len(n)) if n[a-1] < n[a]]
print(new_list)

m = input().split()
n = [int(item) for item in m]
new_list = [n[a] for a in range(1, len(n)) if n[a-1] < n[a]]
print(new_list)
#[12, 44, 4, 10, 78, 123]
#[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]