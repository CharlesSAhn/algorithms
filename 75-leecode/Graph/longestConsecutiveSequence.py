'''

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Approach:
- use set datastructure to store for O(1) lookup.
- check if each num is a starting sequence by checking if i-1 number exist.
- use visit  set to track visited numbers
-

'''


def longestConSecutiveSequence(nums):

    nums_set = set(nums)
    visited = set()
    maxLength = 0

    for num in nums:

        current_length = 1

        prev = num - 1
        if prev not in visited:
            while prev in nums_set:
                current_length += 1
                prev -= 1
                visited.add(prev)

            maxLength = max(maxLength, current_length)

    return maxLength


nums = [100,4,200,1,3,2]
print(longestConSecutiveSequence(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConSecutiveSequence(nums))