import pySerial
import setup
import time


def make_recipe(drink_order):
    arduino = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
    arduino.open()

    for ingredient in drink_order:
        ingredient_name = ingredient[1]
        ingredient_amount = ingredient[0]
        
        setup_pos = setup.get_setup_drinks()[0]
        setup_type = setup.get_setup_drinks()[1]
        
        xpos = setup_pos[ingredient_name]
        
        arduino.write('x\n%s @' % xpos) # Send X axis movement command
        
        arduino.read() # Wait until arduino is finished x axis movement
        
        if setup_type[ingredient_name] == 'spirit': 
            
            # Spirit Behaviour
            
            presses = ingredient_amount / 25 # Convert ml into optic presses
            
            arduino.write('y\n20') # Move Y axis up into dispense position.
            
            while presses > 0:
                arduino.write('y\n10') # Write command to Y axis to raise
                delay(2500) # wait for y axis to raise, dispense liquid, and stop dripping.
                arduino.write('y\n-10')
                delay(1000) # Wait for y axis to retract
                presses = presses - 1
                
            arduino.write('y\n-20') # Move Y axis into travelling position.
            
        else: 
            
            # Mixer behaviour
            
            ml_per_second = 50
            solenoid_id = setup.get_solenoid(ingredient_name) # Get reference number of solenoid valve.
            arduino.write('s\n%s' % solenoid_id) # Cycle Solenoid Valve.
            
            delay_amount = (ml_per_second / 1000) * ingredient_amount
            
            delay(delay_amount) # Leave solenoid open for enough liquid to pass.
            
            arduino.write('s\n%s' % solenoid_id) # Cycle Solenoid Valve.
            
        delay (500) # Delay half a second to catch drips.
        
    arduino.write('x\n0') # Return X axis to zero.
    
