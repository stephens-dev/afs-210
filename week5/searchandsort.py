
from _typeshed import HasFileno
from typing import Sized


def Ordered_binary_Search(olist, item):
    # This function is to divide and conqure by checking if the value is 
    # bigger than the left half or smaller than the right and sending that Half
    # to the other function in order to save time
    
    if len(olist) == 0:
        return False
    else:
        midpoint = len(olist) // 2
        if olist[midpoint] == item:
            return True
        else:
            if item < olist[midpoint]:
                return binarySearch(olist[:midpoint], item)
            else:
                return binarySearch(olist[midpoint+1:], item)


def binarySearch(alist, item):
    # This block of code will will continue to move the midpoint and the last point 
    # to narrow into the value until it is found or the first point is on the right Side 
    # of the last point
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

print(Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
print(Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))
