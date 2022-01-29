'''
Given an integer array, find and return all the subsets of the array.
The order of subsets in the output array is not important. However the order of elements in a particular subset should remain the same as in the input array.

Note: An empty set will be represented by an empty list

Example 1

arr = [9]

output = [[]
          [9]]
Example 2

arr = [9, 12, 15]

output =  [[],
           [15],
           [12],
           [12, 15],
           [9],
           [9, 15],
           [9, 12],
           [9, 12, 15]]
'''

def subset(input):

    return subset2(input, 0)


def subset2(input, index):

    if len(input) == index:

        return [[]]

    result = subset2(input, index + 1)
    output = list()

    # append existing subsets
    for d in result:
        output.append(d)

    # add current elements to existing subsets and add them to the output
    for d in result:
        current = list()
        current.append(input[index])
        current.extend(d)
        output.append(current)


    return output


print(subset([9, 12, 15]))

#input = [9, 12, 15]
#subset(input, 0)
#   subset(input, 1)
#       subset(input, 2)
#           subset(input, 3)
#       result = [[]], output = [[]],  current = [[15], []]
#   result = [[], [15]], output =  [[], [15]]   current = [12]   output =  [[], [15], [12]],   current = [12, 15]