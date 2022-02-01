import pickle

users_parsed = []
i = 0
users_by_hobby = {}
test_of_save = {}
users_file = open('users.csv', 'r', encoding='utf-8')
hobby_file = open('hobby.csv', 'r', encoding='utf-8')
users = users_file.readlines()
hobbys = hobby_file.readlines()
if len(users) < len(hobbys):
    exit(1)
else:
    for i in range(i, len(users)):
        if i <= len(hobbys) - 1:
            users_parsed.append(users[i].replace('\n', '').split(","))
            users_parsed[i] += [hobbys[i].replace('\n', '')]
            users_by_hobby.setdefault(users[i].replace('\n', ''), users_parsed[i])
        else:
            users_by_hobby.setdefault(users[i].replace('\n', ''), None)
users_file.close()
hobby_file.close()
with open('dict_user_by_hobby.pickle', 'wb') as f:
    f.write(pickle.dumps(users_by_hobby))
# далее блок кода в рамках которого мы проверяем корректность записанного файла:
with open('dict_user_by_hobby.pickle', 'rb') as f_1:
    test_of_save = pickle.load(f_1)
print(type(test_of_save))
print(test_of_save)
# далее блок кода в рамках которого можно использовать распарсенные данные:
n = list(users_by_hobby.get((input('Введите ФИО пользователя    ')).replace(' ', ',')))
print(
    f"Хобби пользователя: {n[3]}\nФамилия пользователя: {n[0]}\n"
    f"Имя пользователя: {n[1]}\nОтчество пользователя: {n[2]}", end='')
