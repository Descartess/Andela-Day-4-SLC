""" class that implements binary Search """

class BinarySearch(list):
    """ contains methods that implement binary search"""
    def __init__(self, a, b):
        """initialise the search array"""
        self.extend([num for num in range(0, a*b+1, b)])
        self.length = a
        self.step = b

    def search(self, value):
        count = 0
        found = False
        first = 0
        last = self.length - 1

        while first <= last and not found:
            if not (self[first]<= value <= self[last]):
                  break
            if self[first] == value:
              found = True
              mid = first
            elif self[last] == value:
                found = True
                mid = last
            else:
                mid = (first + last)//2
                if self[mid] == value:
                    found = True
                elif abs(self[mid] - value) < self.step:
                    break
                elif self[mid] < value:
                    first = mid + 1
                else:
                    last = mid - 1
                count += 1
        return {'count':count, 'index':mid} if found else {'count':count, 'index':-1}
