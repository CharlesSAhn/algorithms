'''
In information theory, the Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are different.
Calculate the Hamming distace for the following test cases.

Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance

questions:
- case sensitive?

Approach:
- check two strings' length are equal.
- loop through each characters and check if they are equal.
'''

def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """

    if len(str1) == len(str2):
        count = 0

        for char in range(len(str1)):
            if str1[char] != str2[char]:
                count+=1

        return count

    return None