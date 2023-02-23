'''

You are given an array arr having n integers. You have to find the maximum sum of contiguous subarray among all the possible subarrays.
This problem is commonly called as Maximum Subarray Problem. Solve this problem in O(nlogn) time, using Divide and Conquer approach.

Example 1
Input: arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
Output: Maximum Sum = 10 for the subarray = [5, 0, 3, 2]

Example 2
Input: arr = [-2, -5, 6, -2, -3, 1, 5, -6]
Output: Maximum Sum = 7 for the subarray = [6, -2, -3, 1, 5]

                                [-2, -5, 6, -2, -3, 1, 5, -6]
                           [-2, -5, 6, -2]        [-3, 1, 5, -6]
                     [-2, -5]        [ 6, -2]    [-3, 1]      [5, -6]
                  [-2]    [-5]      [6]  [-2]  [-3]   [1]   [5]    [-6]
                    (   -5   )


'''


def MaxSunArray(nums):
    curSum = 0
    maxsum = -1 * float("inf")

    for num in nums:

        curSum = max(num, curSum + num)
        maxsum = max(curSum, maxsum)

    return maxsum

arr = [-2, 7, -6, 3, 1, -4, 5, 7]
print("Maximum Sum = ",MaxSunArray(arr))

arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
print("Maximum Sum = ",MaxSunArray(arr))

def maxCrossingSum(arr, start_index, mid, end_index):

    leftSum = arr[mid]
    leftMaxSum = arr[mid]

    for i in range(mid-1, start_index, -1):
        leftSum += arr[i]
        if leftSum > leftMaxSum:
            leftMaxSum = leftSum

    rightSum = arr[mid + 1]
    rightMaxSum = arr[mid + 1]

    for j in range(mid + 2, end_index+1):
        rightSum += arr[j]
        if rightSum > rightMaxSum:
            rightMaxSum = rightSum

    return rightMaxSum + leftMaxSum



def getSubArray(arr):

    return getSubArray_helper(arr, 0, len(arr)-1)



def getSubArray_helper(arr, start_index, end_index):

    if start_index == end_index:
        return arr[start_index]

    if start_index < end_index:
        mid = (start_index + end_index) // 2

        L = getSubArray_helper(arr, start_index, mid)
        R = getSubArray_helper(arr, mid + 1, end_index)
        C = maxCrossingSum(arr, start_index, mid, end_index)

        return max(C, max(R, L))



    else:
        return arr[start_index]


# print(getSubArray( [-2, -5, 6, -2, -3, 1, 5, -6]))
#
arr = [-2, 7, -6, 3, 1, -4, 5, 7]
print("Maximum Sum = ",getSubArray(arr))
#
#
# arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
# print("Maximum Sum = ",getSubArray(arr))     # Outputs 10