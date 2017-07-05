""" compares both lists and returns missing value """
def find_missing(array_1, array_2):
    """ compares both lists and returns missing value """
    if len(array_1) == 0 and len(array_2) == 0:
        return 0
    elif len(array_1) > len(array_2):
        missing = list(set(array_1) - set(array_2))
        return int(missing[0])
    elif len(array_1) < len(array_2):
        missing = list(set(array_2) - set(array_1))
        return int(missing[0])
    elif len(array_1) == len(array_2):
        return [ 0 for num in array_1 ]


