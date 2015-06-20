from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel

class DrinkCard(Button):

    def enterDrink(self):
        print 'button pressed'

class BiastApp(App):
    def build(self):
        mainsheet = BoxLayout(orientation='horizontal')

        mainslide = Carousel(direction='right', loop='True', size_hint=(0.8, 0.6), pos_hint_centre=(0.5, 0.5))

        mainslide.add_widget(DrinkCard())
        mainslide.add_widget(DrinkCard())

        mainsheet.add_widget(mainslide)

        return mainsheet


if __name__ == "__main__":
    BiastApp().run()
