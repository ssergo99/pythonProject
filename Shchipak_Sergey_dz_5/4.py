src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []


def bigger_add_func(src_list):
    """The function "bigger_add_func" is used to get an object of the generator class with a sequence of numbers from
    the list (passed to the input of the function) that are in the source list greater than the value of the previous
    element of the source list.

     The main application is the formation of a list of values for fixing the moment of growth of the value, rate,
     level.

     Attributes
    ----------
    src_list : list

     """
    last = max(src_list)
    for num in src_list:

        if num > last:
            yield num
        last = num


result.append(bigger_add_func(src))
print(list(*result))
