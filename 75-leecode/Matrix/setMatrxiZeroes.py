'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.


[
   [1,1,1],
   1,0,1],
   [1,0,0]
]

[
    [1,0,0],
    [0,0,0],
   [0,0,0]
]


if m[i][j] == 0
   - entire i row is 0
   - all row's j is 0

set of rows    (1,2)
set of columns (1,2)

for rows:
    chagne to all 0

    for columns
        change to columne to 0

'''


def setZeros(matrix):

    rows = set()
    columns = set()

    for row_index,row in enumerate(matrix):
        for column_index, column in enumerate(row):
            if matrix[row_index][column_index] == 0:
                rows.add(row_index)
                columns.add(column_index)

    for row_index in range(len(matrix)):

        if row_index in rows:
            for column_index in range(len(matrix[0])):
                print(column_index)
                matrix[row_index][column_index] = 0

        else:
            for column_index in range(len(matrix[0])):
                if column_index in columns:
                    matrix[row_index][column_index] = 0

    return


setZeros([[1,1,1],
    [1,0,1],
    [1,0,0]
]
)