def mk_file_dict(argv):
    program, path_src_file1, path_src_file2, path_targ_file = argv
    import pickle
    src_file1 = str(path_src_file1) + '/users.csv'
    src_file2 = path_src_file2 + '/hobby.csv'
    targ_file = path_targ_file + '/dict_us_by_hob_src.pickle'
    users_parsed = []
    i = 0
    users_by_hobby = {}
    users_file = open(src_file1, 'r', encoding='utf-8')
    hobby_file = open(src_file2, 'r', encoding='utf-8')
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
    with open(targ_file, 'wb') as f:
        f.write(pickle.dumps(users_by_hobby))


if __name__ == '__main__':
    import sys

    exit(mk_file_dict(sys.argv))
