class SkladOrtehnika:
    def __init__(self, name, model, kol):
        self.name = name
        self.model = model
        self.kol = kol
        self.d = {"Марка": self.name, "Модель": self.model, "Количество": self.kol}
        self.pozic = []
        self.vse = []

    def priemka(self):
        try:
            n = input(f'Введите марку: ')
            m = input(f'Введите модель: ')
            k = input(f'Введите количество: ')
            tovar = {'Марка': n, 'Модель': m, 'Количество': k}
            self.d.update(tovar)
            self.pozic.append(self.d)

        except:
            return f"Не правильно введенные данные"

        q = input("Для выхода нажмите Q")
        if q == 'Q' or q == 'q':
            self.vse.append(self.pozic)
            print(f"На складе \n {self.vse}")
        else:
            return SkladOrtehnika.priemka(self)


class Printer(SkladOrtehnika):
    def printer(self):
        print(f"{self.name + ' ' + self.model} Принтер печатает")


class Scanner(SkladOrtehnika):
    def scanner(self):
        print(f"{self.name + ' ' + self.model} Сканнер сканирует")


class Xerox(SkladOrtehnika):
    def xerox(self):
        print(f"{self.name + ' ' + self.model} Ксерокопирование")

org_1 = Printer('hp', '1025', 5)
org_2 = Scanner('canon', '125', 6)
org_3 = Xerox('xerox', '1521', 7)
print(org_1.priemka())
print(org_2.priemka())
print(org_3.priemka())
print(org_1.printer())
print(org_2.scanner())
print(org_3.xerox())