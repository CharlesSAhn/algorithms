'''
The goal of this exercise is to write some code to determine if two strings are anagrams of each other.

An anagram is a word (or phrase) that is formed by rearranging the letters of another word (or phrase).

For example:

"rat" is an anagram of "art"
"alert" is an anagram of "alter"
"Slot machines" is an anagram of "Cash lost in me"
Your function should take two strings as input and return True if the two words are anagrams and False if they are not.

You can assume the following about the input strings:

No punctuation
No numbers
No special characters

Questions:
- can we extra storage?
- case sensitive?


'''


def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """

    # TODO: Write your solution here
    aschii = [0] * 127
    for char in str1:
        if char != " ":
            aschii[ord(char.lower())] += 1

    for char in str2:
        if char != " ":
            aschii[ord(char.lower())] -= 1
            if aschii[ord(char.lower())] < 0:
                return False

    for item in aschii:
        if item != 0:
            return False

    return True