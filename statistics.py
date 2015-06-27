import json

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
    stat_file = open_statistics(drink_id)
