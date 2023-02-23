'''

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Solution:
- use two pointers
 - pointer1 starting substring
 - pointer2 scanning and check if char is repeated in current substring

- currentSubstring
- max length

'''


def lengthOfLongestSubstring(str):

    if len(str) < 2:
        return len(str)

    max = 0

    currentSubstring = ""

    str_list = list(str)

    for index, char in enumerate(str_list):

        if char not in currentSubstring:
            currentSubstring += char

        else:
            if len(currentSubstring) > max:
                max = len(currentSubstring)

            repeated_char_index =  currentSubstring.find(char)
            currentSubstring =  currentSubstring[repeated_char_index + 1: ] + char

    if len(currentSubstring) > max:
        max = len(currentSubstring)

    return max



print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring("bbbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("dvdf"))