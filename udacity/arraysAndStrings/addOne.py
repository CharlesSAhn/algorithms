'''
You are given a non-negative number in the form of list elements.
For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

Example 1:

input = [1, 2, 3]
output = [1, 2, 4]
Example 2:

input = [9, 9, 9]
output = [1, 0, 0, 0]
Challenge:

One way to solve this problem is to convert the input array into a number and then add one to it.
For example, if we have input = [1, 2, 3], you could solve this problem by creating the number 123 and then separating the digits of the output number 124.
'''



def addOne(input):

    add = 2
    for i in range(len(input) , 0, -1):

        # if input[i] + add < 10:
        #     input[i] += 1
        #     break
        #
        # input[i] = 0
        # if i == 0:
        #     input = [1] + input

        res = input[i -1] + add
        if res / 10 == 0:
            input[i] = res
            break

        input[i-1] = res % 10
        if i-1 == 0:
            input = [1] + input



    return input



print(addOne([9,9,9]))
print(addOne([]))
print(addOne([9]))