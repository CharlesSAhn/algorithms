'''
The number of inversions in a disordered list is the number of pairs of elements that are inverted (out of order) in the list.

Here are some examples:

[0,1] has 0 inversions
[2,1] has 1 inversion (2,1)
[3, 1, 2, 4] has 2 inversions (3, 2), (3, 1)
[7, 5, 3, 1] has 6 inversions (7, 5), (3, 1), (5, 1), (7, 1), (5, 3), (7, 3)
The number of inversions can also be thought of in the following manner.

Given an array arr[0 ... n-1] of n distinct positive integers, for indices i and j, if i < j and arr[i] > arr[j] then the pair (i, j) is called an inversion of arr.

[5,7] [1,3] #2
[5,7] [3]   #4
[5,7] []    #6


'''

def inversion(arr):

    arr, counter =  mergesort(arr, 0)

    return counter


def mergesort(arr, counter):

    if len(arr) <= 1:
        return (arr, counter)

    mid = len(arr) // 2

    left = mergesort(arr[:mid], counter)
    right = mergesort(arr[mid:], counter)

    return merge(left, right)




def merge(left, right):

    left_index = 0
    right_index = 0

    counter = left[1] + right[1]

    left = left[0]
    right = right[0]

    merged = []

    while left_index < len(left) and right_index < len(right):


        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])

            temp_left_index = left_index
            while temp_left_index < len(left):
                counter += 1
                temp_left_index += 1

            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged, counter

print(inversion([2,1]))
print(inversion([3, 1, 2, 4]))
print(inversion([7, 5, 3, 1]))
print(inversion([2, 5, 1, 3, 4]))
print(inversion([54, 99, 49, 22, 37, 18, 22, 90, 86, 33]))
print(inversion([1, 2, 4, 2, 3, 11, 22, 99, 108, 389]))

#[1, 2, 4, 2, 3] [ 11, 22, 99, 108, 389]
#[1,2] [4,2,3] [11,22] [99,108,389]
#[1] [2] [4] [2,3] [11][22] [99] [108, 389]
#            [2] [3]             [108] [389]
