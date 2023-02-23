'''

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

i = 0
 - result =


Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Create a list with the product of all elements to the left of each number.
Repeat this process for the right side of each number.
Return the products of both lists at each index

'''

def productExceptSelf2(nums):
    left_products = []
    right_products = []
    result = []

    left_prod = 1
    for num in nums:
        left_products.append(left_prod)
        left_prod *= num

    right_prod = 1
    for num in nums[::-1]:
        right_products.append(right_prod)
        right_prod *= num
    right_products = right_products[::-1]

    return [left * right for left, right in zip(left_products, right_products)]

def productExceptSelf(nums):

    n = len(nums)
    res = [1]*n

    # for prefix
    for i in range(n):
        if i != 0:
            res[i] = res[i-1] * nums[i-1]

    post = nums[n-1] #for postfix

    for i in range(n-1, 0, -1):
        res[i-1] = res[i-1] * post
        post *= nums[i-1]

    return res

print(productExceptSelf2([1,2,3,4]))
