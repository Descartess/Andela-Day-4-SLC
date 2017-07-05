""" compares both lists and returns missing value """
def find_missing(array_1, array_2):
    """ compares both lists and returns missing value """
    if len(array_1) > len(array_2):
        missing = list(set(array_1) - set(array_2))
        return int(missing[0])
    missing = list(set(array_2) - set(array_1))
    return int(missing[0])

