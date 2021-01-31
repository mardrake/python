'''
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''
from random import choice


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"{self.name} {self.color}")

    def go(self):
        print(f"Go-go! car {self.name} with {self.speed}")

    def stop(self):
        print(f"stop {self.name}")

    def turn(self):
        list = ["right", "left"]
        print(f"{self.name} turn {choice(list)}")

    def ShowSpeed(self):
        print(self.speed)

    def police_ident(self):
        if self.is_police == True:
            print('Police')
        else:
            print('No_Police')


class TownCar(Car):
    def speed_high_t(self):
        if self.speed > 60:
            print("Превышение скорости")
        else:
            print(f"Скорость норм {self.speed} км.ч")


class SportCar(Car):
    def speed_high_s(self):
        if self.speed > 350:
            print("Превышение скорости")
        else:
            print(f"Скорость норм {self.speed} км.ч")


class WorkCar(Car):
    def speed_high_w(self):
        if self.speed > 40:
            print("Превышение скорости")
        else:
            print(f"Скорость норм {self.speed} км.ч")


class PoliceCar(Car):
    def speed_high_p(self):
        if self.speed > 100:
            print("Мигалки")
        else:
            print(f"Скорость патруля {self.speed} км.ч")


auto_1 = TownCar(60, 'white', 'Lada', False)
auto_1.go()
auto_1.stop()
auto_1.turn()
auto_1.speed_high_t()
auto_1.police_ident()
print()
auto_2 = WorkCar(30, 'orange', 'JCB', False)
auto_2.go()
auto_2.stop()
auto_2.turn()
auto_2.speed_high_w()
auto_2.police_ident()
print()
auto_3 = SportCar(60, 'red', 'Lambo', False)
auto_3.go()
auto_3.stop()
auto_3.turn()
auto_3.speed_high_s()
auto_3.police_ident()
print()
auto_4 = PoliceCar(50, 'light blue', 'Ford', True)
auto_4.go()
auto_4.stop()
auto_4.turn()
auto_4.speed_high_p()
auto_4.police_ident()
