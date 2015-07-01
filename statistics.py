import time

times_made = dict(
    ginandtonic=1,
    rumandcoke=1
)


def open_statistics(drink_id):
    drink_filepath = '/data/Drinks/' + drink_id + '.txt'
    drink_statistics = open(drink_filepath, 'r+')

    return drink_statistics


def close_statistics(stat_file):
    if stat_file.closed == False:
        stat_file.close()


def drink_made(drink_id):
    timeanddate = time.struftime("Drink made: %a, %H:%M:%S")
    filepath = 'data/Drinks/library/%s.txt' % drink_id
    with open(filepath, 'a') as statfile:
        statfile.write(timeanddate)
