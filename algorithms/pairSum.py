'''
Given an input array and a target value (integer),
find two values in the array whose sum is equal to the target value.
Solve the problem without using extra space. You can assume the array has unique values and will never have more than one solution.

input_list = [2, 7, 9, 10,  11, 15]
target = 13
solution = [2, 11]

sort (inplace sort)
first_index = 0
last_index = len - 1


loop:
 move the last pointer if > target
 if last pointer if < target:

    if first_pinter + last point == target:
        :return

    else if first_pinter + last point > target
        last pointer -= 1
    else:
       first pointer += 1

return -1

'''


def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    TODO: complete this method to find two numbers such that their sum is equal to the target
    Return the two numbers in the form of a sorted list
    """
    arr.sort()

    first_index = 0
    last_index = len(arr) - 1

    while first_index < last_index:

        total = arr[first_index] + arr[last_index]

        if total == target:
            return [arr[first_index], arr[last_index]]

        elif total > target:
            last_index -= 1

        else:
            first_index += 1

    return []


print(pair_sum([ 9, 10,  11, 15, 2, 7], 13))

