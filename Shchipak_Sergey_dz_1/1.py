duration = int(input('Введите значение в секундах:'))
sec = duration % 60
min_full = duration//60
hour_full = duration // 3600
min_ext = duration % 3600
min = min_ext // 60
day_full = duration // 86400
hour_ext = duration % 86400
hour = hour_ext //3600
if duration//60==0:
    print(sec, 'сек')
elif duration//60<60:
    print(min_full, "мин", sec, 'сек')
elif duration//3600<24:
    print(hour_full, "час", min, "мин", sec, 'сек')
else:
    print(day_full, 'дн', hour, "час", min, "мин", sec, 'сек')