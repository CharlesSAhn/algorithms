'''
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.  A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

Input:  Tact Coa
Output:  "taco cat", "atco cta"

Questions:
- what is the role of space?
- ascii characters?
- can I use extra space?
- if input is empty string or " ", is that true?
- if input is one character, true?
- case sensitive?

Assumptions:
- if the origin put has a space, the same number of spaces is included but it won't affect the palindrome requirement.

Approach:
- If number of characters are even:
    - All characters should have a pair
- If number of characters are odd:
    - All characters should have a pair except one.

If extra space is allowed:
1. create a list size of 127 (ascii) - fill with 0
2. use each char aschii number as the index to increment
3. loop through the list and validate.
     - even: either 0 or even number
     - odd: should have only one odd digit.

Run time: O(N)
Space O(N)

'''

def checkPermPalin(input):

    if len(input) < 2:
        return True

    buckets = [0] * 127

    for char in input:
        if char == " ":
            continue
        char = char.lower()
        buckets[ord(char)] += 1


    oddDetected = False

    for num in buckets:
        if num == 0:
            continue
        if num % 2 == 0:
            continue
        else:
            if oddDetected:
                return False
            else:
                oddDetected = True

    return True


print(checkPermPalin("Tact Ca"))