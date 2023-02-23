'''
Question:  Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

[
[1,2,3],
[3,4,5],
[7,0,9],
[10,11,12]
]

Approach:
- detect zero positions
- (i, j)
    ->  entire row i becomes zero
    -> for loop  j becomes zero


Runtime O(N*M) -> in order to visit all matrix

'''


def zero_values(input, matrix):

    for row, col in input:

        # zero row
        for i in range(len(matrix[row])):
            matrix[row][i] = 0

        # zero column
        for j in range(len(matrix)):
            matrix[j][col] = 0

    return matrix

def detect_zero(matrix):

    zero_tuples=[]

    for row in range(0, len(matrix)):

        for column in range(0, len(matrix[0])):

            if matrix[row][column] == 0:
                zero_tuples.append((row, column))

    return zero_tuples

input = [
    [1,2,3],
    [3,4,5],
    [7,0,9],
    [10,11,0]
]
detect = detect_zero(input)
print(zero_values(detect, input))