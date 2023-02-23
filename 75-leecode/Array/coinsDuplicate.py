'''

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

'''

def containDuplciate(input):

    dic = {}

    for num in input:
        if num in dic:
            return True

        dic[num] = 1

    return False

    # return len(input) != len(set(input))


print(containDuplciate([1,2,3,1]))
print(containDuplciate([1,2,3,4]))