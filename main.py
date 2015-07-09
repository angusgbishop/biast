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

        spirits = rawLiquids.ingredientsSplit(drinks.get_drink_recipe(drink_id))[0]
        mixers = rawLiquids.ingredientsSplit(drinks.get_drink_recipe(drink_id))[1]
        for spirit in spirits:
            drink_screen.ids.drink_spirit_list.add_widget(Factory.Separator())
            drink_screen.ids.drink_spirit_list.add_widget(
                Factory.Label(text=str(spirit[0]) + ' parts ' + str(spirit[1])))
        for mixer in mixers:
            drink_screen.ids.drink_mixer_list.add_widget(Factory.Separator())
            drink_screen.ids.drink_mixer_list.add_widget(Factory.Label(text=str(mixer[0]) + ' parts ' + str(mixer[1])))

    def make_drink(self, drink_id):

        drinks.make_drink(drink_id)
        statistics.drink_made(drink_id)

    def backScreen(self):
        self.current = 'Favourites_screen'

    def add_drink(self, drink_name, drink_description, drink_recipe_children, drink_image):
        no_whitespace = drink_name.replace(" ", "")
        new_drink_id = no_whitespace.lower()
        new_file_path = 'data/Drinks/library/%s.txt' % new_drink_id

        drink_recipe = []

        for input_box in drink_recipe_children:
                drink_recipe.append([input_box.parts, input_box.ingredient_name])

        with open(new_file_path, 'w') as new_file:

            new_file.write('drink_id - %s\n' % new_drink_id)
            new_file.write('drink_name - %s\n' % drink_name)
            new_file.write('drink_description - %s\n' % drink_description)
            new_file.write('drink_recipe - %s\n' % drink_recipe)
            new_file.write('END OF DRINK DEFINITION')

        if not new_file.closed:
            new_file.close()

        drinks.import_drink_library()

        self.current = 'Settings_screen'

    def search(self, string_to_search):
        all_drinks = drinks.drink_ids
        print all_drinks
        search_screen_results = self.ids.search_screen_id.ids.search_results

        drinks_found = ['No drinks found with that name! You can add a new one in the settings page.']

        print 'searching for ', string_to_search

        search_screen_results.clear_widgets()

        for drink_id in all_drinks:
            drink_name_trunc = drinks.get_drink_name(drink_id)[:len(string_to_search)]
            print 'checking against:', drink_name_trunc
            if drink_name_trunc.lower() == string_to_search.lower():
                print drink_id
                search_screen_results.add_widget(Factory.Separator())
                button = Factory.DrinkFoundButton()
                button.drink_id = drink_id
                button.text = drinks.get_drink_name(drink_id)
                search_screen_results.add_widget(button)
        search_screen_results.add_widget(Factory.Label())

    def add_drink_box(self):
        self.ids.drink_manager_id.ids.drink_recipe_input.add_widget(Factory.DrinkBox())

    def remove_drink_box(self):
        boxlayout = self.ids.drink_manager_id.ids.drink_recipe_input
        if len(boxlayout.children) > 1:
            boxlayout.remove_widget(boxlayout.children[0])


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


class SettingsScreen_DrinkManger(EmptyScreen):
    pass


class SettingsScreen_BIASTSetup(EmptyScreen):
    pass


class SettingsScreen_NetworkManger(EmptyScreen):
    pass


class SettingsScreen_About(EmptyScreen):
    pass


class SettingsScreen_DrinkManger(EmptyScreen):
    pass


class DrinkCard(BoxLayout):
    pass

class BiastApp(App):
    def build(self):
        drinks.import_drink_library()

        return Screens()


if __name__ == "__main__":
    BiastApp().run()
