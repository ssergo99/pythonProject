class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки {self.title} с помощью ручки")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки {self.title} с помощью карандаша")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки {self.title} с помощью маркера")


a = Pen("яблоко")
b = Pencil("море")
c = Handle("портрет")

a.draw()
b.draw()
c.draw()
