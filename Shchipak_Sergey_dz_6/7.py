def chg_file_sales(argv):
    """The "chg_file_sales" function is used to modify sales data records in the bakery.csv file.
     The arguments passed to the function input set the record number to be changed and the new value of this record.

     The main application of the function is to change the existing array of sales data.

     Attributes
    ----------
    num_to_chg: str
    new_sales: str
    """
    end_of_str = 0

    program, num_to_chg, new_sales = argv

    start = int(num_to_chg)
    sale_fit = format(float(str(new_sales).replace(',', '.')), '09.2f')
    with open('bakery.csv', 'r', encoding='utf-8') as f_1:
        for count_str in f_1:
            end_of_str += count_str.count('\n')
        if start < 1 or start > end_of_str:
            print("Записи с таким номером не существует")
            exit()
    with open('bakery.csv', 'r+', encoding='utf-8') as f_2:
        f_2.seek((start - 1) * 10)
        f_2.write(str(sale_fit)+'\n')


if __name__ == '__main__':
    import sys

    exit(chg_file_sales(sys.argv))
