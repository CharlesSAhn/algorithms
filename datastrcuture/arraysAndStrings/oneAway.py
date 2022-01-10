'''
Questions:  There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits away)

Input:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

"", "" -> true
"b", "" - > true
"ab", "" -> true

questions:
- case sensitive?  a != A ?

Approach:
- check the length of two strings
   if  len_diff > 1:
       return false

when lengths are same:
   - use pointer to scan both string and track differences.  Diff > 1 -> return False     O(N) runtime

when lengths are different:
   - determine the longer word
   - use two pointers to iterate each word
   - i -> scan first word
   - j -> scan second word
   - when diff detected, flag the first diff detection and increment the i by 1 while j stays the same.
        when diff detected but the first detection is already flagged, then return false.

run time - O(N)
space - doesn't use any extra space.

'''


def checkSameLengthWord(word1, word2):

    diff_flag = False
    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            if diff_flag:
                return False
            else:
                diff_flag = True

    return True


def checkOneAwayWords(word1, word2):
    # word1 is always the longer word

    j = 0  # pointer for shorter word

    diff_flag = False

    for i in range(0, len(word1)):

        if word1[i] != word2[j]:
            if diff_flag:
                return False
            else:
                diff_flag = True
                if len(word1) == len(word2):
                    j += 1
        else:
            j += 1

    return True


def secondApproach(word1, word2):

    index1 = 0
    index2 = 0

    diff_flag = False

    while (index1 < len(word1) and index2 < len(word2)):

        if word1[index1] != word2[index2]:
            if diff_flag:
                return False
            else:
                diff_flag = True

                if len(word1) == len(word2):
                    index2 += 1
        else:
            index2 += 1

        index1 += 1

    return True

# pale, ple -> true

def oneAway(word1, word2):

    word1_len = len(word1)
    word2_len = len(word2)

    if abs(word1_len - word2_len) > 1:
        return False

    if word1_len + word2_len < 2:
        return True

    # if word1_len == word2_len:
    #     return checkSameLengthWord(word1, word2)
    # else:
    if word1_len > word2_len:
        return secondApproach(word1, word2)
    else:
        return secondApproach(word2, word1)


# print(oneAway("", ""))  # True
# print(oneAway("a", "")) # True
# print(oneAway("pale", "pale")) #True
print(oneAway("pale", "pade")) #True
print(oneAway("pale", "pzde")) #False
print(oneAway("pale", "ple"))  #True
print(oneAway("pale", "pe"))   #False
print(oneAway("ple", "pale"))  #True