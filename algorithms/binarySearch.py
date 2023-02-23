'''

Find the center of the list (try setting an upper and lower bound to find the center)
Check to see if the element at the center is your target.
If it is, return the index.
If not, is the target greater or less than that element?
If greater, move the lower bound to just above the current center
If less, move the upper bound to just below the current center
Repeat steps 1-6 until you find the target or until the bounds are the same or cross (the upper bound is less than the lower bound).

'''


def start(array, target):
    return binary_search(array, target, 0, len(array))

def binary_search(array, target, first, last):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    if last < first:
        return -1

    mid = (last + first) // 2

    if array[mid] == target:
        return mid

    if target > array[mid]:
        return binary_search(array, target, mid+1, last)

    else:
        return binary_search(array, target, first, mid-1 )



# print(start([7, 8, 9, 10, 11, 12], 10))
print(start([7, 8, 9, 10, 11, 12], 7))
# print(start([7, 8, 9, 10, 11, 12], 12))
# print(start([7, 8, 9, 10, 11, 12], 11))
print(start([7, 8, 9, 10, 11, 12], 8))
