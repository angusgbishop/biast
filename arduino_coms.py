import serial
import setup
import time
import sys
import glob
import errorhandling


def serial_ports():
    """Lists serial ports

    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of available serial ports
    """
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')

    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')

    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def make_recipe(drink_order):
    try:
        arduino = serial.Serial(serial_ports()[0], 9600, timeout=1)
    except IndexError:
        errorhandling.create_error_popup('No Arduino Detected')
        return

    arduino.setDTR(level=False)

    try:
        arduino.open()
    except serial.serialutil.SerialException:
        arduino.close()
        arduino.open()

    while True:
        arduinoread = arduino.readline()
        print 'Arduino: ' + arduinoread
        if 'Ready' in arduinoread:
            break;

    for ingredient in drink_order:
        ingredient_name = ingredient[1].lower()
        ingredient_amount = ingredient[0]

        setup_pos = setup.get_setup_drinks()[0]
        setup_type = setup.get_setup_drinks()[1]

        xpos = setup_pos[ingredient_name]

        print 'Moving to %s' % xpos

        arduino.write('x%s' % xpos)  # Send X axis movement command
        while True:  # Wait until x axis in position
            arduinoread = arduino.readline()
            print 'Arduino: ' + arduinoread
            if 'Moved' in arduinoread:
                break;

        if setup_type[ingredient_name] == 'spirit':

            # Spirit Behaviour

            presses = ingredient_amount / 25  # Convert ml into optic presses

            arduino.write('y\n20')  # Move Y axis up into dispense position.

            while presses > 0:
                print 'Pressing'

                arduino.write('y\n10')  # Write command to Y axis to raise
                time.sleep(2.500)  # wait for y axis to raise, dispense liquid, and stop dripping.
                arduino.write('y\n-10')
                time.sleep(1)  # Wait for y axis to retract
                presses = presses - 1

            arduino.write('y\n-20')  # Move Y axis into travelling position.

        else:

            # Mixer behaviour

            ml_per_second = 50
            solenoid_id = setup.get_solenoid(ingredient_name)  # Get reference number of solenoid valve.
            arduino.write('s\n%s' % solenoid_id)  # Cycle Solenoid Valve.
            print 'Solenoid %s Open' % solenoid_id

            delay_amount = ingredient_amount / ml_per_second

            time.sleep(delay_amount)  # Leave solenoid open for enough liquid to pass.

            arduino.write('s\n%s' % solenoid_id)  # Cycle Solenoid Valve.
            print 'Solenoid %s Closed' % solenoid_id

        time.sleep(0.5)  # Delay half a second to catch drips.

    arduino.write('x\n0')  # Return X axis to zero.
