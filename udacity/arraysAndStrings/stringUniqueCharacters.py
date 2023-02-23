## Question: Implement an algorithm to determine if a string has all unique characters.
##            What if you cannot use additional data structure?


"""
Questions?   ascii string or unicode string?
ASCII: 128 characters, 0-127, 8 bit (byte)
unicode: 2 ^ 21 characters, because unicode characters don't generally fit into 8-bit byte, there are
        numerous ways of storing unicode characters (encoding) in byte sequences, such as UTF-32 and UTF-8.

Can we use additional data structure?
If yes, then we can use dictionary to store each character as key and as we scan through each character, if key already exists,
then answer is no.

For each character:
 - check if key already exists ( O(1) Lookup)
 - if yes: return False
 - if no: add character as key and make value to True.

return True

Run time: O(N) where N is the length of the string
Space: O(N) for dictionary

"""

def uniqueStringChecker(input):

    # dictionary
    char_dic = {}
    for c in input:
        if c in char_dic:
            return False
        else:
            char_dic[c] = True

    return True


## Test cases

input1 = "abcde"
input2 = "abcddee"
input3 = ""

print(uniqueStringChecker(input1))
print(uniqueStringChecker(input2))
print(uniqueStringChecker(input3))


"""
Approach 2 without using additional datastructure.

- Brute force approach.

for each character c:
    scan through the characters on the right side of c being compare to.
    
Running time:
1. O(N)
2. O ( N + (N-1) + .... 1 )   ->  (N + 1) * N/2  -> O(N^2)
          
"""

def uniqueString2(input):

    for i in range(0, len(input)):
        for j in range(i + 1, len(input)):

            if input[i] == input[j]:
                return False

    return True


## Test cases

input1 = "abcde"
input2 = "abcddee"
input3 = ""

print(uniqueString2(input1))
print(uniqueString2(input2))
print(uniqueString2(input3))