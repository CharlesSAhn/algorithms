'''

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.


Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Input: nums = [3,-2,4, -2]
output: 48



Input: nums = [-3,-2,1, -9]
output: 18

Approach:
 case 1)
 all positive [1,2,3] -> product increasing

 case 2)
 all negative [-1, -2, -3] -> best case is -2 * -3

   1) given the first two numbers,   max = 2, min = -2
   2  next multiplcation -> max = 6, min = -6


case 3) edge cse when it has 0 value.
  if 0, reset the max =1 and min = 1
'''


def maxProduct(nums):
    res = max(nums)

    curMin, curMax = 1, 1

    for n in nums:
        if n == 0:
            curMax = 1
            curMin = 1
            continue

        temp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(temp, n * curMin, n)

        res = max(res, curMax)

    return res

# nums = [2,3,-2,4]
# print(maxProduct(nums))

nums = [-2,-7,9 , 0,-1]
print(maxProduct(nums))