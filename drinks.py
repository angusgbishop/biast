import math
import glob

drink_ids = ['ginandtonic', 'rumandcoke']

drink_name = {'ginandtonic': 'Gin & Tonic', 'rumandcoke': 'Cuba Libre'}

drink_description = dict(
    ginandtonic='A gin and tonic is a highball cocktail made with gin and tonic water poured over ice. The cocktail was introduced by the army of the British East India Company in India. In India and other tropical regions, malaria was a persistent problem. In the 1700s it was discovered that quinine could be used to prevent and treat the disease, although the bitter taste was unpleasant. British officers in India in the early 19th century took to adding a mixture of water, sugar, lime and gin to the quinine in order to make the drink more palatable. Soldiers in India were already given a gin ration, and the sweet concoction made sense. Since it is no longer used as an antimalarial, tonic water today contains much less quinine, is usually sweetened, and is consequently much less bitter.',
    rumandcoke='The Cuba Libre, is a highball made of cola, lime, and dark or light rum. This highball is often referred to as a Rum and Coke in the UK where the lime juice may or may not be included. /n Along with the Mojito and the Daiquiri, the Cuba Libre shares the mystery of its exact origin. The only certainty is that this cocktail was first sipped in Cuba. The year? 1900. 1900 is generally said to be the year that cola first came to Cuba, introduced to the island by American troops. But "Cuba Libre!" was the battle cry of the Cuba Liberation Army during the war of independence that ended in 1898.')

drink_img = dict(
    ginandtonic='data/Drinks/ginandtonic.png',
    rumandcoke='data/Drinks/rumAndCoke.png')

drink_recipe = dict(
    ginandtonic=[[1, 'Gin'],
                 [3, 'Tonic Water']],
    rumandcoke=[[1, 'Dark Rum'],
                [3, 'Coke']]
)


def import_drink_library():
    for filename in glob.glob('data/Drinks/library/*.txt'):
        print filename
        with open(filename, 'r') as file:
            for line in file:
                if line[:8] == 'drink_id':
                    print line[11:-1]
                    drink_id = line[11:-1]
                    drink_ids.append(str(drink_id))
                elif line[:17] == 'drink_description':
                    print line[20:]
                    drink_desc = line[20:]
                    drink_description[drink_id] = drink_desc
                elif line[:10] == 'drink_name':
                    print line[13:]
                    drink_nme = line[13:]
                    drink_name[drink_id] = drink_nme
                elif line[:12] == 'drink_recipe':
                    print line[15:]
                    drink_rec = line[15:]
                    drink_recipe[drink_id] = drink_rec


def get_drink_name(drink_id):
    return drink_name[drink_id]


def get_drink_img(drink_id):
    image_pathname = 'data/Drinks/%s.*' % drink_id
    print image_pathname
    return glob.glob(image_pathname)[0]


def get_drink_description(drink_id):
    return drink_description[drink_id]


def get_drink_recipie(drink_id):
    return drink_recipe[drink_id]


def make_drink(drink_id):
    # Calculate volume of cup
    cup_volume = 380

    # Calculate Total number of parts per recipe
    total_parts = 0
    for ingredient in drink_recipe[drink_id]:
        total_parts += ingredient[0]

    # Calculate volume per part
    ingredients_sorted = sorted(drink_recipe[drink_id], key=lambda liquid: liquid[0])

    vol_per_part = math.floor(round((cup_volume / total_parts) / 25) * 25)

    # Calculate Recipe order
    recipe_order = []
    for liquid in drink_recipe[drink_id]:
        recipe_order.append([liquid[0] * vol_per_part, liquid[1]])

    if vol_per_part == 0:
        print 'Glass is not big enough for a serving.'
    else:
        # Send recipe to arduino
        volume_sum = 0
        print 'Making a drink with',
        for ingredient in recipe_order:
            print ' %s ml of %s,' % (ingredient[0], ingredient[1])
            volume_sum += ingredient[0]

        print ' the leftover volume is %s ml' % (cup_volume - volume_sum)
