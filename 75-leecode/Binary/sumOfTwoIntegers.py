'''

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Input: a = 1, b = 2
Output: 3

Constraints:
-1000 <= a, b <= 1000



'''



def getSum(a, b):


    pos_list = []
    neg_list = []

    if a >= 0:
        for i in range(a):
            pos_list.append(0)
    else:
        for i in range(a, 0):
            neg_list.append(0)

    if b >= 0:
        for i in range(b):
            pos_list.append(0)
    else:
        for i in range(b, 0):
            neg_list.append(0)


    if len(pos_list) == 0:

        return -1 * len(neg_list)

    if len(neg_list) == 0:
        return len(pos_list)


    if len(pos_list) >= len(neg_list):

        for i in range(len(neg_list)):
            pos_list.pop()

        return len(pos_list)

    else:
        for i in range(len(pos_list)):
            neg_list.pop()

        return -1 * len(neg_list)



print(getSum(1, 2))
print(getSum(-100, -12))
print(getSum(100, -12))
print(getSum(-100, 12))


