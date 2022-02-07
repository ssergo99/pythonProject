def dir_ext_stat_files(argv):
    """The "dir_ext_stat_files" function is used to get statistics about files (the number of files, in terms
    of their size categories and a list of their extensions) located in the specified directory. The argument passed
     to the function input defines the directory to be analyzed.

     The main use of this function is to search for folders with files that have a large size
     and understand the file extensions with the maximum size.

     Attributes
    ----------
    targ_dir: str
    """
    import os
    import json
    targ_dir = ''
    if len(argv) == 2:
        program, targ_dir = argv
        if not os.path.exists(targ_dir):
            print(f'Указанная директория отсутствует')
            exit(1)
    else:
        print(f'Необходимо указать директорию для анализа')
        exit(2)

    ss = 0
    ss_ext = []
    s = 0
    s_ext = []
    m = 0
    m_ext = []
    b = 0
    b_ext = []
    for root, dirs, files in os.walk(targ_dir):
        for file in files:
            if os.stat(os.path.join(root, file)).st_size < 100:
                ss += 1
                ss_ext.append(file.split('.')[-1])
            elif os.stat(os.path.join(root, file)).st_size < 1000:
                s += 1
                s_ext.append(file.split('.')[-1])
            elif os.stat(os.path.join(root, file)).st_size < 10000:
                m += 1
                m_ext.append(file.split('.')[-1])
            elif os.stat(os.path.join(root, file)).st_size < 100000:
                b += 1
                b_ext.append(file.split('.')[-1])
    dist_stat = {'100': (ss, list(set(ss_ext))), '1000': (s, list(set(s_ext))), '10000': (m, list(set(m_ext))),
                 '100000': (b, list(set(b_ext)))}
    print(dist_stat, type(dist_stat))
    name_file = targ_dir.split("/")[-1]+"_summary.json"
    with open(name_file, 'w', encoding="utf-8") as f:
        f.write(json.dumps(dist_stat))

if __name__ == '__main__':
    import sys

    exit(dir_ext_stat_files(sys.argv))
