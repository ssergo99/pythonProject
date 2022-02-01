import pickle

i = 0
users_by_hobby = {}
test_of_save = {}
users_file = open('users.csv', 'r', encoding='utf-8')
hobby_file = open('hobby.csv', 'r', encoding='utf-8')
users = users_file.read().split("\n")
hobbys = hobby_file.read().split("\n")
if len(users) < len(hobbys):
    exit(1)
else:
    for i in range(i, len(users)):
        if i <= len(hobbys) - 1:
            users_by_hobby.setdefault(users[i].replace('\n', ''), hobbys[i].replace('\n', ''))
        else:
            users_by_hobby.setdefault(users[i].replace('\n', ''), None)
users_file.close()
hobby_file.close()
with open('dict_user_by_hobby.pickle', 'wb') as f:
    f.write(pickle.dumps(users_by_hobby))
with open('dict_user_by_hobby.pickle', 'rb') as f_1:
    test_of_save = pickle.load(f_1)
print(test_of_save)
