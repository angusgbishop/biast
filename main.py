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
        drink_screen = self.ids.drink_screen_id

        drink_screen.drink_id = drink_id
        drink_screen.title_text = drinks.get_drink_name(drink_id)

        drink_screen.ids.drink_description_id.text = drinks.get_drink_description(drink_id)  # Add drink description

        drink_screen.ids.drink_image.source = drinks.get_drink_img(drink_id)  # Add drink image

        drink_screen.ids.drink_spirit_list.clear_widgets()  # Remove any widgets from previous drinks
        drink_screen.ids.drink_mixer_list.clear_widgets()  # Remove any widgets from previous drinks

        spirits = rawLiquids.ingredientsSplit(drinks.get_drink_recipie(drink_id))[0]
        mixers = rawLiquids.ingredientsSplit(drinks.get_drink_recipie(drink_id))[1]
        for spirit in spirits:
            drink_screen.ids.drink_spirit_list.add_widget(Factory.Separator())
            drink_screen.ids.drink_spirit_list.add_widget(
                Factory.Label(text=str(spirit[0]) + ' parts ' + str(spirit[1])))
        for mixer in mixers:
            drink_screen.ids.drink_mixer_list.add_widget(Factory.Separator())
            drink_screen.ids.drink_mixer_list.add_widget(Factory.Label(text=str(mixer[0]) + ' parts ' + str(mixer[1])))

    def make_drink(self, drink_id):

        drinks.make_drink(drink_id)
        statistics.times_made[drink_id] += 1

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
