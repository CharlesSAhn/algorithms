'''

You have been given an array of length = n. The array contains integers from 0 to n - 2.
Each number in the array is present exactly once except for one number which is present twice. Find and return this duplicate number present in the array

Example:

arr = [0, 2, 3, 1, 4, 5, 3]
output = 3 (because 3 is present twice)
The expected time complexity for this problem is O(n) and the expected space-complexity is O(1).

Approach:
O(N) = N-1 + N -2 + N -3 + ... 2  = (N + 2) * N/2  = N^2/2 + 1 -> O(N^2)

Sorting time complexity is O(NlogN)

[0,1,2,2]     -> 5    vs. 6      len(input) - (total - current total)
[0,1,2,2,3]   -> 8    vs. 10     n = 5 - 1
[0,1,2,2,3,4] -> 12   vs. 15     n = 6
[0, 2, 3, 1, 4, 5, 3] -> 18  vs. 21    n = 7
'''


def duplicateNumber(input):

    current_total = 0
    truth_total = 0

    for i in range(0, len(input)):
        current_total += input[i]

    for i in range(0, len(input)-1):
        truth_total += i


    return current_total - truth_total


print(duplicateNumber([0, 2, 3, 1, 4, 5, 3] ))
print(duplicateNumber([0, 2, 3, 1, 4, 5, 3,6,7,8] ))
print(duplicateNumber([0, 2, 2, 1, 4, 5, 3] ))