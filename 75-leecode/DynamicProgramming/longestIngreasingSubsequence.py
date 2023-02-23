'''

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

'''
import sys

def LIS(arr):

    return recursive(arr, 0, len(arr), -sys.maxsize)


# Function to find the length of the longest increasing subsequence
# Run time O(n^2)
def recursive(arr, i, n, prev):

    # Base case: nothing is remaining
    if i == n:
        return 0

    # case 1: exclude the current element and process the
    # remaining elements

    excl = recursive(arr, i + 1, n, prev)

    # case 2: include the current element if it is greater
    # than the previous element in LIS

    incl = 0
    if arr[i] > prev:
        incl = 1 + recursive(arr, i + 1, n, arr[i])

    # return the maximum of the above two choices
    return max(incl, excl)

# # using dynamic programming
def lengthOfList(nums):

    LIS = [1] * len(nums)

    for i in range(len(nums) -1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    return max(LIS)



arr = [0,3,1,2,7]

print(lengthOfList(arr))