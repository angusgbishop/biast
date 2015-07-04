__author__ = 'Angus Bishop'


def get_setup_drinks():
    setup_pos = {}
    setup_type = {}
    with open('data/setup.txt', 'r') as setupfile:
        for line in setupfile:
            if line[0] != '#':
                bottle = []
                separated = line.split(str=',')
                for val in separated:
                    val = val.strip()
                    if not bottle:
                        name = val.lower()
                    elif (val.lower() == 'spirit') or (val.lower() == 'mixer'):
                        dtype = val.lowe()
                    else:
                        pos = eval(val)

                setup_pos[name] = pos
                setup_type[name] = dtype

    return [setup_pos, setup_type]
