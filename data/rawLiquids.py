spirits = [
    'gin',
    'vodka',
    'white rum',
    'dark rum'
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
