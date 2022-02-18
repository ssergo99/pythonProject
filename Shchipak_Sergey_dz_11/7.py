class ComplexNum:
    def __init__(self, dig1, dig2):
        self.dig = complex(dig1, dig2)

    def __add__(self, other):
        self.sum = self.dig + other.dig
        return f"Сумма комплексных чисел {self.dig} и {other.dig} равна {self.sum}"

    def __mul__(self, other):
        self.mul = self.dig * other.dig
        return f"Произведение комплексных чисел {self.dig} и {other.dig} равно {self.mul}"

    def __str__(self):
        return f"Комплексное число: {self.dig}"


m = ComplexNum(2, 3)
n = ComplexNum(5, 6)
print(m)
print(n)
print(m + n)
print(m * n)
