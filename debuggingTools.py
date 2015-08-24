__author__ = 'sgabisho'

import inspect

def debugPrint(text,*args):

    if args is not ():
        importance = args[0].upper()
    else:
        importance = 'INFO' # Default importance value


    if importance == 'HIGH':
        importance_colour = '\033[31m' # Red
        prefix = "[WARNING!          ] "
    elif importance == 'MEDIUM':
        importance_colour = '\033[35m' # Purple
        prefix = "[                  ] "
    elif importance == 'LOW':
        importance_colour = '\033[34m' # Blue
        prefix = "[                  ] "
    elif importance == 'INFO':
        importance_colour = '\033[30m' # Black
        prefix = "[INFO              ] "

    filename = inspect.stack()[1][1].split("\\")[-1]

    print importance_colour + prefix + '\033[1m' + '\033[4m' + "[" + str(filename) + "] " + ':\033[0m '+ text