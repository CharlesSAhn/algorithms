'''
Given an input string, return all permutations of the string in an array.

Example 1:

string = 'ab'
output = ['ab', 'ba']
Example 2:

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']


'''



def permutation(input):

    return return_permutation(input, 0)


def return_permutation(input, index):

    if index >= len(input):
        return [""]

    small_output = return_permutation(input, index + 1)

    output = list()
    current_char = input[index]

    for permutation in small_output:
        for index in range(len(small_output[0] + 1)):
            new_permutation = permutation[0:index] + current_char + permutation[index:]
            output.append(new_permutation)

    return output

