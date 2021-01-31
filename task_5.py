'''
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    title = 'Заголовок'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f"{self.title} Ручкой.")


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f"{self.title} Карандашом.")


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f"{self.title} Маркером.")


p = Pen()
p.draw()
print()
pc = Pencil()
pc.draw()
print()
h = Handle()
h.draw()
