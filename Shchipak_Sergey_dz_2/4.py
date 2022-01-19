bad_words = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор '
                                                                                                        'аэлита']
str_art = []
for value in bad_words:
    str_art = value.split()
    name = str_art.pop()
    welcome = 'Привет, %s!' % (name.title())
    print(welcome)
