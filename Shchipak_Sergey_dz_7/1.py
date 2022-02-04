def make_dir_from_yaml(argv):
    import os
    import yaml

    def make_dir(dict_to_create, from_path):
        for dir_targ in dict_to_create:
            path_dir = os.path.join(from_path, dir_targ)
            if not os.path.exists(path_dir):
                os.makedirs(path_dir)
            else:
                print(f"Директория {path_dir} уже существует.")
            subs = dict_to_create[dir_targ]
            for i in range(0, len(subs)):
                sub = subs[i]
                if type(sub) == str:
                    path_sub = os.path.join(from_path, dir_targ, sub)
                    if not os.path.exists(path_sub):
                        os.makedirs(path_sub)
                    else:
                        print(f"Директория {path_sub} уже существует.")
                else:
                    make_dir(sub, path_dir)

    if len(argv) == 2:
        program, src_file = argv
        if str(src_file).endswith('.yaml'):
            with open(src_file) as f:
                dict_tree = yaml.full_load(f)
        else:
            print(f"Некорректный файл со структурой каталогов. Необходим файл с расширением yaml")
            exit(1)
    else:
        dict_tree = [{'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}]
        with open('dir_tree_templates.yaml', 'w') as f:
            yaml.dump(dict_tree, f)

    start_path = os.getcwd()
    for item in dict_tree:
        current_path = start_path
        make_dir(item, current_path)


if __name__ == '__main__':
    import sys

    exit(make_dir_from_yaml(sys.argv))
