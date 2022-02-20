from random import choice


def get_jokes(n, flag=False):
    """ Создаем генератор шуток """
    for i in range(n):
        random_world_1 = choice(nouns)
        random_world_2 = choice(adverbs)
        random_world_3 = choice(adjectives)
        joke = f'{random_world_1} {random_world_2} {random_world_3}'
        print(joke)
        if flag is True:
            list_2 = joke.split()
            for noun in nouns:
                for fun in list_2:
                    if noun == fun:
                        nouns.remove(noun)
            for adverb in adverbs:
                for fun in list_2:
                    if adverb == fun:
                        adverbs.remove(adverb)
            for adjective in adjectives:
                for fun in list_2:
                    if adjective == fun:
                        adjectives.remove(adjective)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(n=5, flag=True)
