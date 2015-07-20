import time
import drinks
import operator
from kivy.app import App
from kivy.factory import Factory

from kivy.properties import StringProperty

def open_statistics(drink_id):
    drink_filepath = '/data/Drinks/' + drink_id + '.txt'
    drink_statistics = open(drink_filepath, 'r+')

    return drink_statistics


def close_statistics(stat_file):
    if stat_file.closed == False:
        stat_file.close()


def drink_made(drink_id):
    timeanddate = time.strftime("\nDrink made: %a, %H:%M:%S")
    filepath = 'data/Drinks/library/%s.txt' % drink_id
    with open(filepath, 'a') as statfile:
        statfile.write(timeanddate)

def get_favourites():
    times_made = {}
    allids = drinks.get_drink_ids()
    for drinkid in allids:
        filepath = drinks.get_drink_filepath(drinkid)
        with open(filepath, 'r') as file:
            indef = True
            for line in file:
                if not indef:
                    try:
                        times_made[drinkid] += 1
                    except KeyError:
                        print 'statistics.py: %s has been made before, adding to list.' % drinks.get_drink_name(drinkid)
                        times_made[drinkid] = 1
                if 'END OF DRINK DEFINITION' in line:
                    indef = False

    sorteddrinks = sorted(times_made.items(), key=operator.itemgetter(1),reverse=True)
    sorteddrinknames = []
    for drink in sorteddrinks:
        if len(sorteddrinknames) < 5:
            sorteddrinknames.append(drink[0])

    App.get_running_app().root.ids.favourites_screen_id.ids.favs_carousel.clear_widgets()

    for drinkid in sorteddrinknames:
        favscarousel = App.get_running_app().root.ids.favourites_screen_id.ids.favs_carousel

        favdrinkname = drinks.get_drink_name(drinkid)
        favdrinkdesc = drinks.get_drink_description(drinkid)
        favdrinkimag = drinks.get_drink_img(drinkid)

        newDrink = Factory.DrinkCard(drink_name = favdrinkname)
        newDrink.drink_name = favdrinkname
        newDrink.drink_description = favdrinkdesc[:80] + '...'
        newDrink.drink_image = favdrinkimag
        newDrink.drink_id = drinkid

        favscarousel.add_widget(newDrink)

    return sorteddrinknames