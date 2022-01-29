'''
Given an array arr and a target element target, find the last index of occurence of target in arr using recursion. If target is not present in arr, return -1.

For example:

For arr = [1, 2, 5, 5, 4] and target = 5, output = 3

For arr = [1, 2, 5, 5, 4] and target = 7, output = -1


'''

def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    TODO: complete this method to find the last index of target in arr
    """

    return last_index_helper(arr, target, 0)


def last_index_helper(arr, target, index):

    if index >= len(arr):
        return -1

    result = last_index_helper(arr, target, index + 1)

    if arr[index] == target and result == -1:
        result = index

    return result


print(last_index([1, 2, 5, 5, 4], 5))
print(last_index([1, 2, 5, 5, 4], 7))