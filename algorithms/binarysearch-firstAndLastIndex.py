'''
Given a sorted array that may have duplicate values, use binary search to find the first and last indexes of a given value.

For example, if you have the array [0, 1, 2, 2, 3, 3, 3, 4, 5, 6] and the given value is 3, the answer will be [4, 6] (because the value 3 occurs first at index 4 and last at index 6 in the array).

The expected complexity of the problem is  𝑂(𝑙𝑜𝑔(𝑛)) .
'''

def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """

    index = helper(arr, number, 0, len(arr) - 1)

    if index == -1:
        return []

    res = []
    low_index = index
    while arr[low_index] == number and low_index > 0:
        low_index -= 1

    high_index = index
    while arr[high_index] == number and high_index < len(arr) - 1:
        high_index += 1

    low_index = low_index + 1 if low_index > 0 else low_index
    high_index = high_index - 1 if high_index < len(arr) - 1 else high_index

    return [low_index , high_index]

def helper(arr, number, first_index, last_index):

    if first_index > last_index:
        return -1

    mid = (first_index + last_index) // 2

    if arr[mid] == number:
        return mid

    if arr[mid] < number:
        return helper(arr, number, mid + 1, last_index)
    else:
        return helper(arr, number, first_index, mid - 1)


print(first_and_last_index([0,0, 1, 2, 2, 3, 3, 3, 4, 5, 6, 9,9,9], 0))
