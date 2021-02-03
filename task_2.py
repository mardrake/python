'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер ( для пальто) и рост ( для костюма) . Это могут быть обычные числа: V и
H , соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property .
'''
from abc import ABC


class Clothes(ABC):
    def __init__(self, razmer, visota):
        self.v = razmer
        self.h = visota
        # self.__f = 2

    def get_k(self):
        return self.v / 6.5 + 0.5

    def get_p(self):
        return (self.h * 2 + 0.3) / 100

    @property
    def get_all(self):
        return str(f"Сколько ткани надо на пальто и костюм \n"
                   f"{(self.v / 6.5 + 0.5) + ((self.h * 2 + 0.3) / 100)}")


class Palto(Clothes):
    def __init__(self, razmer, visota):
        super().__init__(razmer, visota)
        self.square_p = round(self.v / 6.5 + 0.5)

    def __str__(self):
        return f"На пальто {self.square_p}м"


class Kostume(Clothes):
    def __init__(self, razmer, visota):
        super().__init__(razmer, visota)
        self.square_k = round((self.h * 2 + 0.3) / 100)

    def __str__(self):
        return f"На костюм {self.square_k}м"


palto = Palto(42, 150)
print(palto)
kostume = Kostume(42, 150)
print(kostume)
clothes = Clothes(42, 150)
print(clothes.get_all)
