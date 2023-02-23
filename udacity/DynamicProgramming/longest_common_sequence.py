'''

In text analysis, it is often useful to compare the similarity of two texts (imagine if you were trying to determine plagiarism between a source and answer text).
In this notebook, we'll explore one measure of text similarity, the Longest Common Subsequence (LCS).

The Longest Common Subsequence is the longest sequence of letters that are present in both the given two strings in the same relative order.

Example - Consider the two input strings, str1 = 'ABCD' and str2 = 'AXBXDX'.
The LCS will be 'ABD' with the length as 3 letters. It is because each of the letters 'A' , 'B', and 'D' are present in both the given two strings in the same relative order. Note that:

An LCS need not necessarily be a contiguous substring.
There can be more than one LCS present in the given two strings.
There can be many more common subsequences present here, with smaller length. But, in this problem we are concerned with the longest common subsequence.

'''


def lcs(string_a, string_b):

    matrix = [[0 for _ in range(len(string_a) + 1)] for _ in range(len(string_b) + 1)]

    for char_b_i, char_b in enumerate(string_b):
        for char_a_i, char_a in enumerate(string_a):

            if char_b == char_a:
                matrix[char_b_i + 1][char_a_i +1] = matrix[char_b_i][char_a_i] + 1
            else:
                matrix[char_b_i + 1][char_a_i +1] = max(matrix[char_b_i][char_a_i + 1], matrix[char_b_i + 1][char_a_i])



    print(matrix)
    return matrix[-1][-1]


test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"
print(lcs(test_A1, test_B1))


test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"
print(lcs(test_A2, test_B2))