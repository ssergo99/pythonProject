from abc import ABC, abstractmethod


class AbstractClassWear(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Wear(AbstractClassWear):
    def __init__(self):
        self.name = ''
        self.size_param = 0
        self.consumption = 0

    @property
    def fabric_consumption(self):
        if self.name == 'пальто':
            self.consumption = self.size_param / 6.5 + 0.5
        elif self.name == 'костюм':
            self.consumption = 2 * self.size_param / 100 + 0.3
        else:
            self.name = 'Некорректный тип одежды'
        return f'Для пошива одежды типа "{self.name}" требуется {self.consumption:{3}.{3}} метра ткани'


class Coat(Wear):
    def __init__(self, size):
        Wear.__init__(self)
        self.name = 'пальто'
        self.size_param = size


class Suit(Wear):
    def __init__(self, height):
        Wear.__init__(self)
        self.name = 'костюм'
        self.size_param = height


coat1 = Coat(50)
coat2 = Coat(30)
print(coat1.fabric_consumption)
print(coat2.fabric_consumption)
suit1 = Suit(180)
suit2 = Suit(185)
print(suit1.fabric_consumption)
print(suit2.fabric_consumption)
