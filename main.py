from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

import statistics
import data.drinks


class Screens(ScreenManager):
    def enterDrink(self):
        print 'button pressed'
        name = '1'
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
            self.current = self.previous()
            print self.current


class EmptyScreen(Screen):
    pass

class FavouritesScreen(Screen):
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
