def num_odd_gen(end_of_nums):
    """The function "num_odd_gen" is used to get an object of the generator class with a sequence of odd numbers in
    the range between 1 and the value passed to the function input.

    The main application is the formation of a list of positive odd numbers in a given range.

    Attributes
    ----------
    end_of_nums : int

    """

    for num in range(1, end_of_nums + 1, 2):
        yield num


list_of_nums = num_odd_gen(int(input("Введите число окончания диапазона   ")))
print(*list_of_nums)
