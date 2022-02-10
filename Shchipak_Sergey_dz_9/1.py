import time


class TrafficLight:
    __color = ''

    def running(self):
        n = 1
        while n > 0:
            TrafficLight.__color = "\033[33m {}".format("yellow")
            TrafficLight.cls(TrafficLight.__color)
            time.sleep(2)
            TrafficLight.__color = "\033[32m {}".format("green")
            TrafficLight.cls(TrafficLight.__color)
            time.sleep(5)
            TrafficLight.__color = "\033[31m {}".format("red")
            TrafficLight.cls(TrafficLight.__color)
            time.sleep(7)

    @staticmethod
    def cls(color_now):
        print("\n" * 20)
        print(color_now)


lights = TrafficLight()
lights.running()
