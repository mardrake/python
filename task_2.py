class MyOwnEr(Exception):
    def __init__(self, txt):
        self.txt = txt
k=5
while k>0:
    in_data = input("Любое число:")
    out_data = input("На что делим:")
    try:
        in_data = int(in_data)
        out_data = int(out_data)
        if out_data == 0:
            raise MyOwnEr("На ноль делить нельзя!!!")
    except (ValueError, MyOwnEr) as err:
        print(err)
    else:
        print(f"Ответ: {in_data/out_data}")
    finally:
        k-=1
        print(f"Расчет окончен, осталось {k} попытки")