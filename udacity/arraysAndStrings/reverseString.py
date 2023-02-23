'''
In this first exercise, the goal is to write a function that takes a string as input and then returns the reversed string.

For example, if the input is the string "water", then the output should be "retaw".
'''


def reverse(input):

    new_str = ""

    for i in range(len(input)):
        new_str += input[len(input) - i - 1]

    return new_str

print(reverse("Water"))