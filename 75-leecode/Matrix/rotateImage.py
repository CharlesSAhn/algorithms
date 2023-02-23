'''

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

'''


def rotate(matrix):

    left, right = 0, len(matrix) - 1


    while left < right:

        top, buttom = left, right

        for i in range(right - left):

            topLeft = matrix[top][left + i]

            matrix[top][left + i] = matrix[buttom - i][left]

            matrix[buttom - i][left] = matrix[buttom][right - i]

            matrix[buttom][right - i] = matrix[top + i][right]

            matrix[top + i][right] = topLeft

        left += 1
        right -= 1

    return matrix

matrix = [ [5,1,9,11],
           [2,4,8,10],
           [13,3,6,7],
           [15,14,12,16]
           ]
print(rotate(matrix))


'''
[ [5,1,9,11],
  [2,4,8,10],
  [13,3,6,7],
  [15,14,12,16]
]

[
  [15,12,2,5],
  [14,6,3,13],
  [10,8,4,9],
  [16,7,1,11]]

'''

