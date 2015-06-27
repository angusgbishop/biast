spirits = [
    'gin',
    'vodka',
    'white rum',
    'dark rum',
    'tequila',
    'schnapps',
    'whiskey'
]


def isSpirit(drink):
    drink_is_spirit = False
    for tested_drink in spirits:
        if drink.lower() == tested_drink:
            drink_is_spirit = True
    return drink_is_spirit


def ingredientsSplit(drink_recipie):
    spirits_and_mixers = []
    spirits = []
    mixers = []
    for ingredient in drink_recipie:
        if isSpirit(ingredient[1]):
            spirits.append(ingredient)
        else:
            mixers.append(ingredient)

    spirits_and_mixers = [spirits, mixers]

    for lst in spirits_and_mixers:
        if lst == []:
            lst.append('None!')

    return spirits_and_mixers
