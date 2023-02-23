'''

Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]


1. first row  (first row index += 1)
2. and the end of the row, column down (end_index -= 1)
3. print reverse order of the last row (last row -= 1)
4. first column upto first row

'''

# first_row_index = 0
# end_column_index = len(matrix[0])
# last_row_index = len(matrix)
# first_column_index = 0

#stop when:
# first_row_index == last_row_index  or end_column_index == first_column_index


def spiralMatrix(matrix):

    first_row_index = 0
    first_column_index = 0
    last_row_index = len(matrix) - 1
    end_column_index = len(matrix[0]) -1

    output = list()

    totalNumber = len(matrix) * len(matrix[0])

    while first_row_index <= last_row_index and first_column_index <= end_column_index:

        for column in range(first_column_index, end_column_index + 1):
            output.append(matrix[first_row_index][column])

        first_row_index += 1

        if first_row_index > last_row_index:
            break

        for row in range(first_row_index, last_row_index + 1):
            output.append(matrix[row][end_column_index])

        end_column_index -= 1

        if first_column_index > end_column_index:
            break

        for column in range(end_column_index, first_column_index - 1, -1 ):
            output.append(matrix[last_row_index][column])

        last_row_index -= 1


        for row in range(last_row_index, first_row_index - 1, -1):
            output.append(matrix[row][first_column_index])

        first_column_index += 1


    return output


print(spiralMatrix([[1,2,3],[4,5,6],[7,8,9]]))

print(spiralMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(spiralMatrix([[1,2],[3,4],[5,6], [7,8]]))

print(spiralMatrix([[7],[9],[6]]))

