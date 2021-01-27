'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
t = 0
q = 1
m = 0
with open("my_file2.txt", 'w', encoding='utf-8') as my_file:
    num = int(input('Введите число отличное от нуля: '))
    while num != 0:
        print(q, 'число равно:', num)
        q = q + 1
        my_file.write(f"{num}")
        my_file.write(' ')
        num = num - 1
with open("my_file2.txt", 'r', encoding='utf-8') as my_file_r:
    print(my_file_r.read())
with open("my_file2.txt", 'r', encoding='utf-8') as my_file_r:
    for line in my_file_r:
        for i in line.split():
            m = m + int(i)
print('Сумма чисел прочитав файл: ', m)
