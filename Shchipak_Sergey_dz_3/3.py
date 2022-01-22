def thesaurus(*args):
    """
    The "thesaurus" function is used to get a dictionary of names sorted by key values
    - the initial letters of names.

 The main application is the formation of registers of people according to the alphabetical principle.

 Attributes
----------
list of names : tulip
 a tuple with a list of names to sort by first letter of name
    """
    names = [*args]
    my_dict = {}
    for name in names:
        first_let = name[0]
        names_now = [name]
        if my_dict.get(first_let):
            names_now += my_dict.get(first_let)
        now_dict = {first_let: names_now}
        my_dict.update(now_dict)

    return my_dict


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Игорь', 'Прасковья', 'Алексей', 'Александр'))
