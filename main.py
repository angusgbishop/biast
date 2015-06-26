from kivy.app import App

from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition
from kivy.factory import Factory

import statistics
import drinks
import rawLiquids


class Screens(ScreenManager):
    transition = RiseInTransition()

    def enterDrink(self, drink_id):
        self.current = 'drink_screen'
        print drinks.get_drink_name(drink_id)
        self.ids.drink_screen_id.title_text = drinks.get_drink_name(drink_id)
        self.ids.drink_screen_id.ids.drink_description_id.text = drinks.get_drink_description(drink_id)
        spirits = rawLiquids.ingredientsSplit(drinks.get_drink_recipie(drink_id))[0]
        mixers = rawLiquids.ingredientsSplit(drinks.get_drink_recipie(drink_id))[1]
        print spirits
        # Factory.Label(text = spirit[0] + ' parts ' + spirit[1])    Factory.Separator
        for spirit in spirits:
            print (str(spirit[0]) + ' parts ' + str(spirit[1]))
            self.ids.drink_screen_id.ids.drink_spirit_list.add_widget(Factory.Separator())
            self.ids.drink_screen_id.ids.drink_spirit_list.add_widget(
                Factory.Label(text=str(spirit[0]) + ' parts ' + str(spirit[1])))
        for mixer in mixers:
            print (str(mixer[0]) + ' parts ' + str(mixer[1]))
            self.ids.drink_screen_id.ids.drink_mixer_list.add_widget(Factory.Separator())
            self.ids.drink_screen_id.ids.drink_mixer_list.add_widget(
                Factory.Label(text=str(mixer[0]) + ' parts ' + str(mixer[1])))

    def makeDrink(self,drink_to_make):

        drinks.makeDrink(drink_to_make)
        statistics.drink_to_make.times_made += 1


    def backScreen(self):
        if self.current == "DrinkScreen":
            previousScreen = self.current
            self.current = self.previous()
            self.remove_screen(previousScreen)
        elif self.current == 'Favourites_screen':
            pass
        else:
            self.current = 'Favourites_screen'


class EmptyScreen(Screen):
    title_text = StringProperty('')

class FavouritesScreen(EmptyScreen):
    pass

class DrinkScreen(EmptyScreen):
    pass


class SettingsScreen(EmptyScreen):
    pass

class SearchScreen(EmptyScreen):
    pass


class SelectionScreen(EmptyScreen):
    pass


class DrinkCard(BoxLayout):
    pass


class BiastApp(App):
    def statistics():
        pass

    def build(self):

        return Screens()


if __name__ == "__main__":
    BiastApp().run()
