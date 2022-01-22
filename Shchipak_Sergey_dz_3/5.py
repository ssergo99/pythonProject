import random

"""
The "get_jokes" function is used to get a selected number of jokes
made up of arbitrary combinations of nouns, adjectives and adverbs.

 The main application is to use as a random triples generator 
 nouns, adjectives, and adverbs.

 Attributes
----------
the number of comic sentences and the flag of the possibility of repeating sentences:
enter the value of the number of sentences, set the flag of the possibility of repeating
 a comic sentence
"""


def get_jokes(quant_of_jokes, doubles=False):
    jokes = {}
    i = 1
    y = 0
    nouns = ["автомобиль", "лес", "огонь", "город", "дом", "слон"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "мягкий"]
    while i < len(nouns) * len(adverbs) * len(adjectives):
        for noun in nouns:
            for adverb in adverbs:
                for adjective in adjectives:
                    joke = {i: [noun, adverb, adjective]}
                    jokes.update(joke)
                    i += 1
    if doubles:
        while y < quant_of_jokes:
            print(jokes.get(random.randint(1, 120)))
            y += 1
    else:
        print(random.choices(jokes, k=quant_of_jokes))


get_jokes(int(input('Введитеколичество шуток для вывода:  ')))
