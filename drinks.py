drink_ids = ['ginandtonic', 'rumandcoke']

drink_name = {'ginandtonic': 'Gin & Tonic', 'rumandcoke': 'Cuba Libre'}

drink_description = dict(
    ginandtonic='A gin and tonic is a highball cocktail made with gin and tonic water poured over ice. /n The cocktail was introduced by the army of the British East India Company in India. In India and other tropical regions, malaria was a persistent problem. In the 1700s it was discovered that quinine could be used to prevent and treat the disease, although the bitter taste was unpleasant. British officers in India in the early 19th century took to adding a mixture of water, sugar, lime and gin to the quinine in order to make the drink more palatable. Soldiers in India were already given a gin ration, and the sweet concoction made sense. Since it is no longer used as an antimalarial, tonic water today contains much less quinine, is usually sweetened, and is consequently much less bitter.',
    rumandcoke='The Cuba Libre, is a highball made of cola, lime, and dark or light rum. This highball is often referred to as a Rum and Coke in the UK where the lime juice may or may not be included. /n Along with the Mojito and the Daiquiri, the Cuba Libre shares the mystery of its exact origin. The only certainty is that this cocktail was first sipped in Cuba. The year? 1900. 1900 is generally said to be the year that cola first came to Cuba, introduced to the island by American troops. But "Cuba Libre!" was the battle cry of the Cuba Liberation Army during the war of independence that ended in 1898.')

drink_img = dict(
    ginandtonic='data/Drinks/ginAndTonic.png',
    rumandcoke='data/Drinks/rumAndCoke.png')

drink_recipie = dict(
    ginandtonic=[[1, 'Gin'],
                 [3, 'Tonic Water']],
    rumandcoke=[[1, 'Dark Rum'],
                [3, 'Coke']]
)


def get_drink_name(drink_id):
    return drink_name[drink_id]


def get_drink_description(drink_id):
    return drink_description[drink_id]


def get_drink_recipie(drink_id):
    return drink_recipie[drink_id]
