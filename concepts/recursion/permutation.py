'''

Let's use recursion to help us solve this permutation problem:

Given a list of items, the goal is to find all of the permutations of that list.
For example, if given a list like: ["apple", "water"], you could create two permuations from it.
One in the form of the original input and one in the reversed order like so: ["water","apple"]

'''


import copy

def permute(input):
    """
    Return a list of permutations

    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]
       [0, 1, 2] -> [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

    Args:
      l(list): list of items to be permuted

    Returns:
      list of permutation with each permuted item being represented by a list
    """

    perm = []
    if len(input) == 0:
        perm.append([])
    else:
        first = input[0]
        after_first = slice(1, None)
        sub_permute = permute(input[after_first])

        for p in sub_permute:
            for j in range(0, len(p) + 1):
                r = copy.deepcopy(p)
                r.insert(j,first)
                perm.append(r)

    return perm

print(permute([0, 1]))



#permute([0,1])
#   first = 0
#   sub_permute = permute([1])
#                     first = 1
#                     sub_permute = permute([])
#                     sub_permute = [[]]
#                     perm = [[1]]
#   sub_permute = [[1]]
#   p = [1], j = 0, r = [1] -> [0,1], perm = [[0,1]]
#            j = 1, r = [1] -> [1,0], perm = [[0,1], [0,1]]
