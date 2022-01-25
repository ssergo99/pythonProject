def num_translate(digit):
    """The "num_translate" function is used to get the Russian equivalent of the English version
of writing a number from 1 to 10

 The main application is the replacement of lowercase spellings of English numbers with Russian analogues.

 Attributes
----------
eng_digit : str
english number from 1 to 10 inclusive
    """
    dig = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
           'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    return dig.get(digit)


eng_dig = input('Input digit in English   ')
print('In Russian it calls:' + ' ' + num_translate(eng_dig))