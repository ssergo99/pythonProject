class OwnZeroDivError(Exception):
    def __init__(self, txt):
        self.txt = txt


first_param = int(input("Введите делимое: "))
try:
    second_param = int(input("Введите делитель: "))
    if second_param == 0:
        raise OwnZeroDivError("Ошибка! Вы пытаетесь делить на 0!")
except ValueError:
    print("Вы ввели не число")
except OwnZeroDivError as err:
    print(err)
else:
    print(f"Результат деления: {(first_param / second_param)}")
