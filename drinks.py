import math
import glob
import arduino_coms

drink_ids = []

drink_name = {}

drink_description = {}
drink_img = {}

drink_recipe = {}


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
                    drink_desc = line[20:-1]
                    drink_description[drink_id] = drink_desc
                elif line[:10] == 'drink_name':
                    print line[13:]
                    drink_nme = line[13:-1]
                    drink_name[drink_id] = drink_nme
                elif line[:12] == 'drink_recipe':
                    print line[15:]
                    drink_rec = line[15:]
                    drink_recipe[drink_id] = eval(drink_rec)
                elif line == 'END OF DRINK DEFINITION':
                    break



def get_drink_name(drink_id):
    return drink_name[drink_id]

def get_drink_img(drink_id):
    image_pathname = 'data/Drinks/%s.*' % drink_id
    print image_pathname
    image = glob.glob(image_pathname)
    if image == []:
        return 'data/Drinks/no_image.jpg'
    else:
        return image[0]


def get_drink_description(drink_id):
    return drink_description[drink_id]


def get_drink_recipe(drink_id):
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

    arduino_coms.make_recipe(recipe_order)
