__author__ = 'Angus Bishop'


def get_setup_drinks():
    setup_pos = {}
    setup_type = {}
    with open('data/setup.txt', 'r') as setupfile:
        for line in setupfile:
            if line[0] != '#' and line != '':
                pos = 0
                dtype = ''
                name = ''
                separated = line.split(',')
                for val in separated:
                    val = val.strip()
                    if not name:
                        name = val.lower()
                    elif (val.lower() == 'spirit') or (val.lower() == 'mixer'):
                        dtype = val.lower()
                    else:
                        pos = eval(val)
                setup_pos[name] = pos
                setup_type[name] = dtype

    return [setup_pos, setup_type]

def get_solenoid(drink_id):
    solenoid_number = 'No Solenoid Found'
    with open('data/setup.txt', 'r') as setupfile:
        for line in setupfile:
            if line[0] != '#' and line != '\n':
                separated = line.split(',')
                if (separated[0].lower() == drink_id) and (separated[1].lower().strip() == 'mixer'):
                    solenoid_number == separated[3].strip()

                    print separated[3].strip()
    return solenoid_number