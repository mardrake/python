# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
input_number = int(input('''Введите месяц в формате (1 - 12)
------------------------------ 
программа отобразит время года:'''))
calendar_list = ['Зима', 'Весна', 'Лето', 'Осень']
calendar_dict = {1: "Зима", 2: "Весна", 3: "Лето", 4: "Осень"}
if input_number <= 0 or input_number > 12:
    print('Такого времения года не существует')
elif 3 <= input_number <= 5:
    print('Время года', calendar_list[1], '(список)')
    print('Время года', calendar_dict[2], '(словарь)')
elif 6 <= input_number <= 8:
    print('Время года', calendar_list[2], '(список)')
    print('Время года', calendar_dict[3], '(словарь)')
elif 9 <= input_number <= 11:
    print('Время года', calendar_list[3], '(список)')
    print('Время года', calendar_dict[4], '(словарь)')
else:
    print('Время года', calendar_list[0], '(список)')
    print('Время года', calendar_dict[1], '(словарь)')