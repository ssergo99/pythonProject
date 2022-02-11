class Road:

    def __init__(self):
        self._lenght = 0
        self._width = 0

    def weight(self, lenght, width):
        self._lenght = lenght
        self._width = width
        weight_road_tn = self._lenght * self._width * 25 * 5 / 1000
        print(f"Масса асфальта, необходимого для покрытия всей дороги длиной {self._lenght} метров "
              f"и шириной {self._width} метров: {weight_road_tn} тонн")


road1 = Road()
road1.weight(5000, 10)
