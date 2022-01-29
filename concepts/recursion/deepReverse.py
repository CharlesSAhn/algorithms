'''
Define a procedure, deep_reverse, that takes as input a list, and returns a new list that is the deep reverse of the input list.
This means it reverses all the elements in the list, and if any of those elements are lists themselves,
reverses all the elements in the inner list, all the way down.

Note: The procedure must not change the input list itself.


input = [1,2,3,4]
input = [1, [1,2,3],4]

'''


def reverse(input):

    return helper_reverse(input, 0)


def helper_reverse(input, index):

    if index == len(input):
        return []


    incomplete_response = helper_reverse(input, index + 1)

    append = input[index]
    if isinstance(input[index], list):
        sub_list = input[index]
        append = helper_reverse(sub_list, 0)

    incomplete_response.append(append)

    return incomplete_response


print(reverse([1,2,3,4]))
print(reverse([1, [1,2,3],4]))