class Complexxx:
    def __init__(self, a_1, a_2):
        self.a_1 = a_1
        self.a_2 = a_2

    def __add__(self, other):
        self.summa_a_1 = self.a_1 + other.a_1
        self.summa_a_2 = self.a_2 + other.a_2

    def __mul__(self, other):
        self.mul_a_1 = self.a_1 * other.a_1 - self.a_2 * other.a_2
        self.mul_a_2 = self.a_2 * other.a_1 - self.a_1 * other.a_2


a = Complexxx(float(2), float(3))
b = Complexxx(float(4), float(5))
a + b
a * b
print('Сумма:   %.2f+%.2fj' % (a.summa_a_1, a.summa_a_2))
print('Произв.: %.2f+%.2fj' % (a.mul_a_1, a.mul_a_2))
