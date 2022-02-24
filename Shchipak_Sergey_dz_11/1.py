class DateClass:

    def __init__(self, date_str):
        self.date = date_str

    @classmethod
    def date_pars(cls, date):
        day = int(date.split('-')[0])
        month = int(date.split('-')[1])
        year = int(date.split('-')[2])
        if cls.date_virify(day, month, year):
            return day, month, year
        else:
            return f"Скорректируйте значение даты: {date}"

    @staticmethod
    def date_virify(day, month, year):
        day_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        if 0 < year < 2100:
            if 0 < month < 13:
                if 0 < day < (day_in_month.get(month) + 1):
                    return True
                else:
                    print(f"Некорректный формат дня. Должен быть в диапазоне от 1 до {day_in_month.get(month)}. "
                  f"Ваше значение {day}.")
                    return False
            else:
                print(f"Некорректный формат месяца. Должен быть в диапазоне от 1 до 12. Ваше значение {month}.")
                return False
        else:
            print(f"Некорректный формат года. Должен быть в диапазоне от 1 до 2099. Ваше значение {year}.")
            return False


m = DateClass('15-04-2002')
n = DateClass('31-04-2002')
t = DateClass('31-13-2002')
print(m.date)
print(n.date)
print(t.date)
print(DateClass.date_pars(m.date))
print(DateClass.date_pars(n.date))
print(DateClass.date_pars(t.date))
