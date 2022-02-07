def dir_stat_filesize(argv):
    """The "dir_stat_filesize" function is used to get statistics about files (the number of files, in terms of their
    size categories) located in the specified directory. The argument passed to the function input
    defines the directory to be analyzed.

     The main use of this function is to search for folders with files that have a large size.

     Attributes
    ----------
    targ_dir: str
    """
    import os
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
    s = 0
    m = 0
    b = 0
    for root, dirs, files in os.walk(targ_dir):
        for file in files:
            if os.stat(os.path.join(root, file)).st_size < 100:
                ss += 1
            elif os.stat(os.path.join(root, file)).st_size < 1000:
                s += 1
            elif os.stat(os.path.join(root, file)).st_size < 10000:
                m += 1
            elif os.stat(os.path.join(root, file)).st_size < 100000:
                b += 1
    dist_stat = {'100': ss, '1000': s, '10000': m, '100000': b}
    print(dist_stat, type(dist_stat))


if __name__ == '__main__':
    import sys

    exit(dir_stat_filesize(sys.argv))
