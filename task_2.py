class MyOwnEr(Exception):
    def __init__(self, txt):
        self.txt = txt


class Myclass:
    @staticmethod
    def staticmethod(c, d):
        try:
            c = int(c)
            d = int(d)
            if d == 0:
                raise MyOwnEr("На ноль делить нельзя!!!")
        except (ValueError, MyOwnEr) as err:
            print(err)
        else:
            print(f"Ответ: {c / d}")

my = Myclass()
my.staticmethod(4, 0)
