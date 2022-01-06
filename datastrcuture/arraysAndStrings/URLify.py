'''
Question: Write a method to replace all spaces in a string with "%20"
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the true length of the string.

Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"

Question:
- ascii character?
- can you have multiple white spaces consecutively?
- sufficient space at the end -> will that be just enough or could have more than enough so I need to calculate?

Approach 1:
- get the space count and use that to calculate the last index.
- shift characters from backward.   O(N)
    - use two pointers, one for new position and one for old position.
- if white spaces, decrease the pointer by three positions.

N: length of input
Run time: O(N)
Space: O(N)

'''


def replaceWhiteSpace(input, length):

    input_list = list(input)

    whiteSpaces = 0
    for char in range(0, length):
        if input_list[char] == " ":
            whiteSpaces += 1

    new_i = length + 2 * whiteSpaces - 1
    current_i = length - 1


    while current_i > -1:
        if input[current_i] == " ":
            input_list[new_i] = "0"
            input_list[new_i - 1] = "2"
            input_list[new_i - 2] = "%"
            new_i = new_i -3
        else:
            input_list[new_i] = input_list[current_i]

            new_i -= 1

        current_i -= 1


    result = "".join(input_list)
    return result.lstrip()

print(replaceWhiteSpace("Mr John Smith    ", 13))
print(replaceWhiteSpace(" Mr John Smith      ", 14))
print(replaceWhiteSpace("smith", 5))
print(replaceWhiteSpace("   ", 1))