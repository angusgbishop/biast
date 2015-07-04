import pySerial
import setup


def make_recipe(drink_order):
    arduino = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
    arduino.open()

    for ingredient in drink_order:
        ingredient_name = ingredient[1]
        ingredient_amount = ingredient[0]

        setup_pos = setup.get_setup_drinks()[0]
        setup_type = setup.get_setup_drinks()[1]

        xpos = setup_pos[ingredient_name]

        arduino.write('x\n%s @' % xpos)

        arduino.read()

        if setup_type[ingredient_name] == 'spirit':
            # Convert ml into optic presses
            presses = ingredient_amount / 25
        else:
            ml_per_second = 50
