'''
Questions: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?

[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]


[
 [7,4,1],
 [8,5,2],
 [9,6,3]
]

(0,2) -> (0,0)

'''

def rotate(input):

    n = len(input)

    if n == 0 or n != len(input[0]):
        return False

    for layer in range(0, int(n/2)):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first

            top = input[first][i]  # save top

            #left -> top
            input[first][i] = input[last - offset][first]

            #buttom -> left
            input[last - offset][first] = input[last][last-offset]

            #right -> buttom
            input[last][last-offset] = input[i][last]

            #top right
            input[i][last] = top


    return input


input = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotate(input))
