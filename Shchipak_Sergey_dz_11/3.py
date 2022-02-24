class OwnDigitError(Exception):
    def __init__(self, txt):
        self.txt = txt


m = 0
list_of_dig = []
while m == 0:
    val = input("Введите значение для формирования списка: ")
    try:
        if val == 'stop':
            m = 1
        elif val.isdigit():
            list_of_dig.append(val)
        else:
            raise OwnDigitError("Веденное значение не является числом")
    except OwnDigitError as err:
        print(err)
print(f'Список чисел: {list_of_dig}')
