'''
Given an input_list and a target, return the indices of pair of integers in the list that sum to the target.
The best solution takes O(n) time. You can assume that the list does not have any duplicates.

For e.g. input_list = [1, 5, 9, 7] and target = 8, the answer would be [0, 3]


dic = {
    abs(number - target): index
    7 : 0
    3: 1
    1: 3
}
for loop list
 - abs(num - target)

'''

def pair_sum_to_zero(input_list, target):
    # TODO: Write pair sum to zero function

    dic = {}

    for index in range(0, len(input_list)):

        num = input_list[index]

        if num in dic:
            return [index, dic[num]]
        if num <= target:
            diff = abs(num - target)
            dic[diff] = index



print(pair_sum_to_zero([1, 5, 9, 7], 8))