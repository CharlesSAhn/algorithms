'''

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

'''


def comb(nums, target):
    cache = {}
    result =  combinationSum4(nums, target, cache)
    print(cache)
    return result

def combinationSum4(nums, target, cache):


    if target < 0:
        return 0

    if target == 0:

        return 1

    total = 0

    if target in cache:
        return cache[target]

    else:
        for num in nums:
            total += combinationSum4(nums, target - num, cache)

        cache[target] = total
        return total



print(comb([1,2,3], 4))

