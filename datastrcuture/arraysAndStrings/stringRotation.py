'''
Question:  Assume you have a method isSubstring which checks if one word is substring of another.  Given two strings,
s1 and s2, write code to check if s2 is a rotation of s1 using one call to isSubstring.

ex. "waterbottle" -> "erbottlewat"

Approach:
- is length same?
- "waterbottlewaterbottle"  ->s1s1

s2 will be a substring of s1s1


'''

def isRotation(s1, s2):

    if len(s1) != len(s2) or len(s1) > 0:
        return False

    return isSubstring(s1s1, s2)