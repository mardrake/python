'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__() ), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — с истема некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
'''


class Matrix():
    def __init__(self, matrix):
        self.s = '\n'.join(['\t'.join([str(j) for j in i]) for i in matrix])
        list = []
        for el in matrix:
            list.append([ej for ej in el])
        self.matrix = matrix

    def __add__(self, other):
        NumStr = len(self.matrix)
        NumCol = len(other.matrix[0])
        for el in range(NumStr):
            for ej in range(NumCol):
                self.matrix[el][ej] = self.matrix[el][ej] + other.matrix[el][ej]
            Result = self.matrix
        return Matrix(Result)

    def __str__(self):
        self.t = str(self.s)
        return self.t


m_1 = Matrix([[31, 22], [37, 43], [51, 86]])
print(m_1)
print()
m_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, -64, 8]])
print(m_2)
print()
m_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(m_3)
print()
m_4 = Matrix([[16, 17, 18], [19, 20, 21], [22, 23, 24]])
m_5 = Matrix([[25, 26, 27], [16, 17, 18], [19, 20, 21]])
print(m_4 + m_5)
