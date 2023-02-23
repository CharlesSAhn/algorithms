
'''
In general, a palindrome is a string that reads the same backwards as forwards, e.g., MADAM.
In the last notebook, we saw that in a given string, a subsequence is an ordered set of characters that need not necessarily be a contiguous substring, e.g.,
ABC is a subsequence in AXBYC with length = 3.

The Longest Palindromic Subsequence (LPS) is the most lengthy sequence of characters that is a palindrome.
In this notebook, you'll be tasked with finding the length of the LPS in a given string of characters.

Examples:

With an input string, MAXDYAM, the LPS is MADAM, which has length = 5
With an input string, BxAoNxAoNxA, the LPS is ANANA, which has length = 5
With an input string, BANANO, the LPS is NAN, which has length = 3
With an input string, ABBDBCACB, the LPS is BCACB, which has length = 5


  B A N A N O
B
A
N
A
N
O

'''


def lps(input_string):

    # The function should return one value: the LPS length for the given input string

    # Start with an n x n matrix where n is the number of characters in a given string.
    # The diagonal cells should all have the value 1 for the base case, the rest can be zeros.

    n = len(input_string)

    L = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        L[i][i] = 1

    for s_size in range(2, n+1):
        for start_idx in range(n - s_size+1):
            end_idx = start_idx + s_size - 1

            if s_size == 2 and input_string[start_idx] == input_string[end_idx]:
                # match with a substring of length 2
                L[start_idx][end_idx] = 2

            elif input_string[start_idx] == input_string[end_idx]:
                # general match case
                L[start_idx][end_idx] = L[start_idx+1][end_idx-1] + 2
            else:
                # no match case, taking the max of two values
                L[start_idx][end_idx] = max(L[start_idx][end_idx-1], L[start_idx+1][end_idx]);




print(lps("BxAoNxAoNxA"))