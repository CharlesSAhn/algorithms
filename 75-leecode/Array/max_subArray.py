'''

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]

Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23

Approach:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]

max = 0

i = 0  accum = -2  ->  accum = 0
i = 1  accum = 1
i = 2  accum = -2  ->. accum = 0
i = 3  accum = 4
i = 4  accum = 3
i = 4  accum = 5
i = 5  accum = 6  max = 6
i = 6  accum = 1
i = 7  accum = 5    -> index = 3 and end-index = 7

'''




def maxSubArray(nums):

    max = 0
    current_sum = 0

    for num in nums:
        current_sum += num

        if current_sum > 0:
            if current_sum > max:
                max = current_sum

        else:
            current_sum = 0

    return max






nums = [5,4,-1,7,8]
print(maxSubArray(nums))

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))




