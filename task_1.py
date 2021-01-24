'''
 Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. 
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''
from sys import argv

script_name, virab, stavka, premiya = argv


def itog():
    while True:
        try:
            v = int(virab)
            s = int(stavka)
            p = int(premiya)
            if v > 0 and s > 0 and p > 0:
                itogo = (v * s) + p
                print('Все круто, поздравляю с премией!')
                break
            elif v <= 0 and s > 0 and p > 0:
                print('Вы ошиблись Выработка должна быть, ставлю минималку час : ')
                itogo = s + p
                break
            elif v > 0 and s <= 0 and p > 0:
                print('Считаю по минимальной ставке 2 rub : ')
                itogo = (v * 2) + p
                break
            elif v > 0 and s > 0 and p < 0:
                print('И как мы отнимем премию? : ')
                itogo = v * s
                break
            elif v > 0 and s > 0 and p == 0:
                print('Ничего страшного премия будет ещё: ')
                itogo = v * s
                break
            elif v <= 0 and s > 0 and p <= 0:
                print('Вы ошиблись Выработка должна быть, ставлю минималку час : ')
                itogo = v * s
                break
            else:
                print('Не надо мудрить!!!')
                itogo = 0
                break

        except ValueError:
            print('Не надо мудрить!!!')
            itogo = 0
            break
    return itogo


print("Имя скрипта: ", script_name)
print("Выработка в часах: ", virab)
print("Ставка в час: ", stavka)
print("Премия : ", premiya)
print("Итого : ", itog(), 'rub')
