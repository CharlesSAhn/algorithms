'''
You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

Example 1:

arr= [1, 2, 3, -4, 6]
The largest sum is 8, which is the sum of all elements of the array.
Example 2:

arr = [1, 2, -5, -4, 1, 6]
The largest sum is 7, which is the sum of the last two elements of the array.



'''


def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    current_sum = arr[0]
    max_sum = arr[0]

    for num in arr:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)

    return max_sum


print(max_sum_subarray([1, 2, -5, -4, 1, 6]))