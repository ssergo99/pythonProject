def thesaurus_adv(*args):
    """
    The "thesaurus" function is used to get a dictionary of names and surnames sorted by key values
    - the initial letters of surnames.

 The main application is the formation of registers of people according to the alphabetical principle.

 Attributes
----------
list of names and surnames:  tulip
 a tuple with a list of names to sort by first letter of surname
    """
    names = [*args]
    my_dict = {}
    for namesurname in names:
        list_surname = namesurname.split(' ')
        surname = list_surname[1]
        first_let = surname[0]
        if my_dict.get(first_let):
            namesurname = my_dict.get(first_let) + "," + namesurname
        now_dict = {first_let: namesurname}
        my_dict.update(now_dict)

    return my_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))