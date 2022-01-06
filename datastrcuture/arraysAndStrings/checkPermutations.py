'''
Question:  Given two strings, write a method to decide if one is a permutation of other.

Permutation of "hello" {"elloh", "ollhe", "llohe"}

If they are permutation of another:
 - length of strings are equal
 - the count of each character is equal

Assumption:
 - use extra space?
 - is case sensitive?
 - is whitespace significant?

Approach is:
  1. check if both strings sizes are equal, if not return false.
  2. store characters from the first string as a key for dictionary and set the value to 1 (or increment by 1 if already exists)
  3. loop through the second string and check if each character exists in the dic.
     - if it doesn't exist, return False
     - if exists:
             - if that key's value is < 1, return False.


sample input:
- "hello", "lloh"
- "", "ada"
- "", ""
- "hello", "heloo"

{ "h": 1,  -> 0
  "e": 1,  -> 0
  "l": 2,  -> 1
  "o": 1   -> 0  refurn false
}

N: length of string
Run time: O(N)
Space: O(N)

'''


def isPerm(str1, str2):

    if len(str1) != len(str2):
        return False

    dict = {}

    str1.strip()
    str2.strip()

    for char in str1:

        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    for char2 in str2:
        if char2 not in dict:
            return False
        if dict[char2] < 1:
            return False
        dict[char2] -= 1

    return True

print(isPerm("hello", "HELLO"))
print(isPerm("hello", "elloh"))
print(isPerm("hello", "Elloh"))
print(isPerm("hello ", "elloh "))
print(isPerm("", "ada"))
print(isPerm("", ""))
print(isPerm("hello", "heloo"))


'''
Second approach

1. check if both have the same length
2. sort both strings.
3. scan both strings and check if both strings has same characters
'''