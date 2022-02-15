class Cell:

    def __init__(self, count_cell):
        self.count = int(count_cell)
        self.str_to_print = ''

    def __add__(self, other):
        self.add_new = self.count + other.count
        return Cell(self.add_new)

    def __sub__(self, other):
        self.sub_new = self.count - other.count
        if self.sub_new >= 0:
            return Cell(self.sub_new)
        else:
            return f"Второе значение меньше первого!!!"

    def __mul__(self, other):
        self.mul_new = self.count * other.count
        return Cell(self.mul_new)

    def __floordiv__(self, other):
        self.floordiv_new = self.count // other.count
        return Cell(self.floordiv_new)

    def __truediv__(self, other):
        self.truediv_new = self.count / other.count
        return Cell(self.truediv_new)

    def make_order(self, cells_in_row):
        full_row = self.count // cells_in_row
        not_full_row = self.count % cells_in_row
        if not_full_row == 0:
            self.str_to_print = ((cells_in_row * '*') + '\n') * full_row
        else:
            self.str_to_print = ((cells_in_row * '*') + '\n') * full_row + not_full_row * "*"
        return self.str_to_print

    def __str__(self):
        return f'{self.count}'


a = Cell(36)
b = Cell(16)
print(a + b)
print(a - b)
print(b - a)
print(a * b)
print(a // b)
print(a / b)
print(a.make_order(4))
print(b.make_order(5))
