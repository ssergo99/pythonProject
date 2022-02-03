def show_file_sales(argv):
    """The "show_file_sales" function is used to output sales data records from the bakery.csv file.
    The arguments passed to the function input set the number of the initial record for output and
    the number of the final record for output. When passing only one argument to the function, the
    output range is set from the record number equal to the passed attribute to the end of the list of records.
     When running the function without attributes, the output range is set from the beginning of the list of records
     to the end of the list of records.

     The main application of the function is to output the required array of sales data.

     Attributes
    ----------
    start_arg: str (optional)
    finish_arg: str (optional)
    """
    end_of_str = 0
    if len(argv) == 3:
        program, start_arg, finish_arg = argv
    elif len(argv) == 2:
        program, start_arg = argv
        finish_arg = 1
    else:
        start_arg = 1
        finish_arg = 1
    start = int(start_arg)
    finish = int(finish_arg)
    with open('bakery.csv', 'r', encoding='utf-8') as f_1:
        if finish == 1:
            for count_str in f_1:
                end_of_str += count_str.count('\n')
            finish = end_of_str
        f_1.seek((start - 1) * 10)
        for ind in range(start, finish+1):
            print(format(float((f_1.readline().strip())), '9.2f'))


if __name__ == '__main__':
    import sys

    exit(show_file_sales(sys.argv))
