'''

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".


Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Brute Force:
for loop s:


'''


def wordBreakDP(s, wordDict):

    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) -1, -1, -1):
        for w in wordDict:

            if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                dp[i] = dp[i + len(w)]

            if dp[i]:
                break

    return dp[0]



def wordBreak(index, s, wordDict):

    if index == len(s):
        return True

    for i in wordDict:

        if s[index:index + len(i)] == i:

            res =  wordBreak(index + len(i), s, wordDict)

            if res:
                return True

    return False


print(wordBreak(0,  "cars", ["car","ca","rs"]))
print(wordBreakDP( "applepenapple", ["apple","pen"]))
print(wordBreakDP( "catsandog", ["cats","dog","sand","and","cat"]))