'''

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

'''

import collections

def initailizer():
    return 0

def isAnagram(s, t):

    if len(s) < 1 or len(t) < 1:
        return False

    map = collections.defaultdict(initailizer)

    for char in s:
        map[char] += 1

    for char in t:
        if char not in map:
            return False
        map[char] -= 1

        if map[char] < 0:
            return False

    for index, value in map.items():
        if value > 0:
            return False


    return True




s = "anagram"
t = "nagaram"

print(isAnagram(s,t))

s = "rat"
t = "car"
print(isAnagram(s,t))