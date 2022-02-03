def mk_file_sales(argv):
    """The "mk_file_sales" function is used to record sales data passed to the function input in the bakery.csv file.

     The main application of the function is the formation of an array of sales data.

     Attributes
    ----------
    sale: str

     """
    program, sale = argv
    sale_fit = format(float(str(sale).replace(',', '.')), '09.2f')
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(str(sale_fit)+'\n')


if __name__ == '__main__':
    import sys

    exit(mk_file_sales(sys.argv))
