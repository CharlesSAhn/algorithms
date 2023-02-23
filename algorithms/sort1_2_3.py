'''

Write a function that takes an input array (or Python list) consisting of only 0s, 1s, and 2s, and sorts that array in a single traversal.

Note that if you can get the function to put the 0s and 2s in the correct positions, this will aotumatically cause the 1s to be in the correct positions as well.

test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]

pointer1 -  where 0 ends
poitner2 - where 2 starts

[0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2] zero_index = 0  prev_index = 10 two_index = 10

[0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2] zero_index = 0  prev_index = 9 two_index = 9

[0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2] zero_index = 1  prev_index = 9 two_index = 9

[0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2] zero_index = 2  prev_index = 9 two_index = 9

[0, 0, 0, 2, 2, 1, 1, 1, 2, 2, 2] zero_index = 3  prev_index = 9 two_index = 9

[0, 0, 0, 2, 2, 1, 1, 1, 2, 2, 2] zero_index = 3  prev_index = 8 two_index = 8

[0, 0, 0, 2, 2, 1, 1, 1, 2, 2, 2] zero_index = 3  prev_index = 7 two_index = 7

[0, 0, 0, 2, 2, 1, 1, 1, 2, 2, 2] zero_index = 3  prev_index = 7 two_index = 6

[0, 0, 0, 2, 2, 1, 1, 1, 2, 2, 2] zero_index = 3  prev_index = 7 two_index = 5

[0, 0, 0, 2, 2, 1, 1, 1, 2, 2, 2] zero_index = 3  prev_index = 7 two_index = 4

[0, 0, 0, 2, 1, 1, 1, 2, 2, 2, 2] zero_index = 3  prev_index = 6 two_index = 4

[0, 0, 0, 2, 1, 1, 1, 2, 2, 2, 2] zero_index = 3  prev_index = 6 two_index = 3

[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2] zero_index = 3  prev_index = 5 two_index = 2

pointer1
'''


def sort123(arr):

    zero_index = 0
    two_index = len(arr) - 1

    prev_index = len(arr) - 1

    while zero_index <= two_index:

        if arr[two_index] == 2:
            arr[prev_index], arr[two_index] = arr[two_index], arr[prev_index]
            two_index -= 1
            prev_index -= 1

        elif arr[two_index]  == 0:
            arr[zero_index], arr[two_index] = arr[two_index], arr[zero_index]
            zero_index += 1

        else:
            two_index -= 1

    return arr

print(sort123([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))



