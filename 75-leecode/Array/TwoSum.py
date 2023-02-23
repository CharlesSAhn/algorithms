'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Assumption:
- target > 0
- cant use number twice
- numbers in the list are > 0-
-

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Approaches:
 - sort the list   nlogn
 - two pointers
 -  start_index = 0
 -  end_index = -1

 While Looping:
    check of both values = target
        return
   - if both values  > target:
        end_index -= 1
    else:
         start_index += 1


Approach #2:
 - use dictionary
 - loop:
   - if value in dict:
      return [ value in the dic, current index]
   - dist[ target - value] = value index


   return -1

'''



def twoSum( nums, target):


    dict = {}

    for index, value in enumerate(nums):

        if value in dict:

            return[dict[value], index]

        dict[target - value] = index



input = [-3,4,3,90]
target = 0


print(twoSum(input, target))