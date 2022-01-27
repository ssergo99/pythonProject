i = 0
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Федор']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']
tut_by_klasses = ((tutors[i], klasses[i]) if i <= len(klasses) - 1 else (tutors[i], None)
                  for i in range(i, len(tutors)))
print(type(tut_by_klasses))
print(next(tut_by_klasses, 'Значения закончились'))
print(next(tut_by_klasses, 'Значения закончились'))
print(next(tut_by_klasses, 'Значения закончились'))
print(next(tut_by_klasses, 'Значения закончились'))
print(next(tut_by_klasses, 'Значения закончились'))
print(next(tut_by_klasses, 'Значения закончились'))
print(next(tut_by_klasses, 'Значения закончились'))
print(next(tut_by_klasses, 'Значения закончились'))
print(next(tut_by_klasses, 'Значения закончились'))
