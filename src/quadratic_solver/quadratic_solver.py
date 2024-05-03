import math


class QuadraticSolver:
    def __init__(self, a, b, c):
        self.a = self.validate(a)
        self.b = self.validate(b)
        self.c = self.validate(c)


    @staticmethod
    def validate(n):
        if isinstance(n, float):
            return n
        elif isinstance(n, int):
            return float(n)
        elif isinstance(n, str):
            try:
                return float(n)
            except ValueError:
                raise
        else:
            raise TypeError

    def equation(self):
        return f'{self.a}*x**2 + {self.b}*x + {self.c} = 0'

    def determinant(self):
        d = self.b ** 2 - 4 * self.a * self.c
        return d

    def solve(self):
        d = self.determinant()
        if d < 0:
            raise ValueError('Negative determinant')
        x1 = (-self.b + math.sqrt(d)) / (2 * self.a)
        x2 = (-self.b - math.sqrt(d)) / (2 * self.a)
        return x1, x2