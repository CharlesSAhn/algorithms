'''

Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.

For exmaple, if n = 4, then output = [1, 4, 6, 4, 1].

0:     1       only =1
1:    1 1     first and last is 1.
2:   1 2 1    Odd: 2/3 = 1 middel is index 1
3:  1 3 3 1   even: 4/2 = 2 ->  middle is 1 and 2
4: 1 4 6 4 1  odd: 5/2 = 2  -> middle  increment by index after `.
5:1 5 10 10 5 1   (1) (i) (i + i) (i + i) (i) 1
prev = []
current = []]
loop:
- if len == 1:
      current.append(1)
      prev.append(1)

  if len ==2 :

'''


def trianble(depth):

    # prev = [1]
    #

    if depth == 0:
        return [1]

    prev = None
    for i in range(0, depth + 1):

        current = [1]
        for j in range(1, i+1):

            num = prev[j-1] + prev[j]
            current.append(num)

        current.append(1)
        prev = current

    return current

#
print(trianble(0))
print(trianble(1))
print(trianble(2))
print(trianble(3))
print(trianble(4))
print(trianble(5))