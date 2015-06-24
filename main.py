from kivy.app import App

from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition

import statistics
import data.drinks


class Screens(ScreenManager):
    transition = RiseInTransition()

    def enterDrink(self, drink_id):
        print 'button pressed'
        name = '1'
        self.title_text = str(drink_id)
        newDrink = DrinkScreen(name=name)
        self.add_widget(newDrink)
        self.current = name

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
