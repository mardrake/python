class MyOwnEr(Exception):
    def __init__(self, txt):
        self.txt = txt


a = []


class MyClass:
    @staticmethod
    def staticmethod(c):
        try:
            # c = int(c)
            if type(c) == int or type(c) == float:
                a.append(c)
                print(f"Добавил в список {c}")
            else:
                raise MyOwnEr(f"Не будет в списке этой кракозябры: {c}")
        except (ValueError, MyOwnEr) as err:
            print(err)
        else:
            print(f"Список состоит из последовательности чисел{list(a)}")


my = MyClass()
my.staticmethod(4)
my.staticmethod(5)
my.staticmethod(6)
my.staticmethod("dsadasd")
my.staticmethod(7)


# Прицеплю заодно еще кое-что
class MyOwnEr(Exception):
    def __init__(self, txt):
        self.txt = txt


a = []

while True:
    in_data = input("Любое число или q для выхода:")
    if in_data == 'q':
        break
    try:
        in_data = int(in_data)
        if type(in_data) == int or type(in_data) == float:
            a.append(in_data)
        else:
            raise MyOwnEr("К сожалению это не число")
    except (ValueError, MyOwnEr) as err:
        print(err)
    else:
        print(f"Ответ: {list(a)}")
