class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        return f"Автомобиль {self.name} цвета {self.color} поехал"

    def stop(self):
        return f"Автомобиль {self.name} цвета {self.color} остановился"

    def turn(self, direction):
        return f"Автомобиль {self.name} цвета {self.color} повернул на {direction}"

    def show_speed(self):
        return f"Скорость автомобиля {self.name} цвета {self.color} составляет {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            return f"Вы превышаете установленное ограничение (60 км/ч)по скорости. Ваша скорость {self.speed}"
        return f"Скорость автомобиля {self.name} цвета {self.color} составляет {self.speed}"


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            return f"Вы превышаете установленное ограничение (40 км/ч) по скорости. Ваша скорость {self.speed}"
        return f"Скорость автомобиля {self.name} цвета {self.color} составляет {self.speed}"


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


a = SportCar(156, 'red', "Bugatti")
b = WorkCar(45, 'black', "Ford")
c = PoliceCar(86, 'blue', "BMW")
d = TownCar(75, 'white', "Opel")

print(f"Название авто: {a.name}")
print(f"Цвет авто: {a.color}")
print(f"Полицейская машина: {a.is_police}")
print(a.show_speed())
print("---------------------------")
print(f"Название авто: {c.name}")
print(f"Цвет авто: {c.color}")
print(f"Полицейская машина: {c.is_police}")
print(c.show_speed())
print("---------------------------")
print(f"Название авто: {b.name}")
print(f"Цвет авто: {b.color}")
print(f"Полицейская машина: {b.is_police}")
print(b.show_speed())
print("---------------------------")
print(d.go())
print(d.stop())
print(d.turn("право"))
