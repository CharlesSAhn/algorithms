'''

Given a string consisting of uppercase and lowercase ASCII characters, write a function, case_sort,
that sorts uppercase and lowercase letters separately, such that if the  𝑖 th place in the original string had an uppercase character
then it should not have a lowercase character after being sorted and vice versa.

For example:
Input: fedRTSersUXJ
Output: deeJRSfrsTUX

'''

def mergeSort(input):

    if len(input) <= 1:
        return input

    mid = len(input) // 2

    left = mergeSort(input[:mid])
    right = mergeSort(input[mid:])

    return merge(left, right)


def merge(left, right):

    left_index = 0
    right_index = 0

    merged = []

    while left_index < len(left) and right_index < len(right):
        if ord(left[left_index]) <= ord(right[right_index]):
            merged.append(left[left_index])
            left_index += 1

        else:
            merged.append((right[right_index]))
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list

    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character

    Uppoer case: A -> 65 Z ->90, a->97 z -> 122

    """
    lower_case = []
    upoer_case = []

    for char in string:
        if ord(char) > 96:
            lower_case.append(char)
        else:
            upoer_case.append(char)

    sorted_lower = mergeSort(lower_case)
    sorted_upper = mergeSort(upoer_case)

    print(sorted_lower)
    print(sorted_upper)

    final = []
    left_index = 0
    right_index = 0
    for index in range(len(string)):
        if ord((string[index])) > 96:
            final.append(sorted_lower[left_index])
            left_index += 1
        else:
            final.append((sorted_upper[right_index]))
            right_index += 1

    return "".join(final)


def case_sort2(string):
    input = list(string)
    sorted_input = mergeSort(input)


    final = []
    left_index = 0
    right_index = 0

    for index, char in enumerate(sorted_input):
        if ord(char) > 96:
            left_index = index
            break


    for index in range(len(string)):
        if ord((string[index])) > 96:
            final.append(sorted_input[left_index])
            left_index += 1
        else:
            final.append((sorted_input[right_index]))
            right_index += 1

    return "".join(final)


print(case_sort2('fedRTSersUXJ'))