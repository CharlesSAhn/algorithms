'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

'''
import collections

def def_value():
    return 0



def minWindow(s, t):

    '''
    Run time: O(2 * N + M)
    M: length of t
    N: length of s
    '''

    if len(s) == 0 or s is None or t is None or len(t) == 0:
        return ""

    #initial character counter for t.
    map = collections.defaultdict(def_value)

    for char in t:
        map[char] += 1

    i, j = 0, 0
    counter = len(map)
    left = 0
    right = len(s)

    min = len(s)
    found = False

    while j < len(s):

        if s[j] in map:
            map[s[j]] -= 1

            if map[s[j]] == 0:
                counter -= 1

        j += 1

        if counter > 0:
            continue

        while counter == 0:

            if s[i] in map:
                map[s[i]] += 1

                if map[s[i]] > 0:
                    counter += 1
            i += 1

        if (j - i) < min:
            left = i
            right = j
            min = j - i

            found = True



    if found:
        return s[left-1: right]
    else:
        return ""





print(minWindow("ADOBECODEBANC", "ABC"))