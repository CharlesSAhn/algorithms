'''

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

Apporoach


'''
from collections import defaultdict

def chracterReplacement2(s, k):

    left = maxlen = maxrepeat = 0
    counts = defaultdict(int)

    for right in range(len(s)):
        counts[s[right]] += 1

        #here we're trying to determine the amount of repeating characters of any count. Later on, we will be replacing them anyway
        maxrepeat = max(maxrepeat, counts[s[right]])

        #here, if the remaining letters are greater than k, we need to shrink our sliding window
        if (right-left+1 - maxrepeat) > k:
            counts[s[left]] -= 1 #delete the values previously seen in our hashmap
            left += 1            # slide the window over by one

        maxlen = max(maxlen, right-left+1)

    return maxlen




def chracterReplacement(s, k):

    if k >= len(s):
        return len(s)

    if len(s) < 2:
        return len(s)

    max = 1
    original_k = k
    first_character_change_index = None
    scanning_index = 1
    current_repeated_count = 1
    starting_character = s[0]

    string_length = len(s)
    while len(s) > scanning_index:

        if starting_character == s[scanning_index]:
            scanning_index +=1
            current_repeated_count += 1

            if current_repeated_count > max:
                max = current_repeated_count
        else:
            if k > 0:
                if first_character_change_index is None:
                    first_character_change_index = scanning_index

                k -= 1
                current_repeated_count += 1
                scanning_index += 1

                if current_repeated_count > max:
                    max = current_repeated_count
            else:
                current_repeated_count = 0
                starting_character = s[scanning_index]
                k = original_k
                if first_character_change_index is not None:
                    scanning_index = first_character_change_index
                first_character_change_index = None

    return max

#
# print(chracterReplacement("ABAB", 2))
# print(chracterReplacement("ABAB", 1))

print(chracterReplacement2("AABABBAAAAAAA", 1))

#print(chracterReplacement2("AAAB", 0))

