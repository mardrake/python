class Data:
    def __init__(self, day, month, year):
        self.d = day
        self.m = month
        self.y = year

    @classmethod
    def int_data(cls, int_data):
        day, month, year = map(int, int_data.split('-'))
        return day, month, year

    @staticmethod
    def data_prov(int_data):
        day, month, year = map(int, int_data.split('-'))
        return day<=31, month<=12, year<=2021

data = Data.data_prov('31-12-2001')
print(data)
data = Data.int_data('31-12-2001')
print(data)
