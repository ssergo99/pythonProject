class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 0, "bonus": 0}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position)
        self.wage = wage
        self.bonus = bonus

    def get_full_name(self):
        return f"Полное имя: {self.surname} {self.name}"

    def get_total_income(self):
        self._income = {"wage": self.wage, "bonus": self.bonus}
        return f"Общий доход: {sum(self._income.values())}"


a = Position("Mike", "Jones", "Manager", 10, 15)
b = Position("Steve", "Davis", "Accountant", 7, 10)
print(f"Имя: {a.name}")
print(f"Фамилия: {a.surname}")
print(f"Должность: {a.position}")
print(a.get_total_income())
print(a.get_full_name())
print("---------------------------")
print(f"Имя: {b.name}")
print(f"Фамилия: {b.surname}")
print(f"Должность: {b.position}")
print(b.get_total_income())
print(b.get_full_name())
