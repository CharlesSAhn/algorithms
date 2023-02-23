'''

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

'''

from collections import defaultdict

def groupAnagrams(input):

    dic = defaultdict(list)

    for item in input:

        count = [0] * 26

        for char in item:
            count[ord(char) - ord("a")] += 1

        dic[tuple(count)].append(item)

    return dic.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

strs = ["a"]
print(groupAnagrams(strs))

strs = [""]
print(groupAnagrams(strs))