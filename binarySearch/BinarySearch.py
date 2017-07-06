""" class that implements binary Search """

class BinarySearch(object):
    """ contains methods that implement binary search"""
    def __init__(self, a, b):
        """initialise the search array"""
        self.array = [ num for num in range(a*b, b)]

        
