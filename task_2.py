'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''
class Road:
    def __init__(self, _length, _width, massa = 25, chislo = 5):
        self.massa = massa
        self.chislo = chislo
        self.width = _width
        self.length = _length

    def rasch(self):
        self.length * self.width * self.massa * self.chislo / 1000
        print(f"{int(self.length * self.width * self.massa * self.chislo / 1000)}" + ' ''Tonn')


r = Road(5000, 20)
r.rasch()
