'''
A child is running up a staircase with and can hop either 1 step, 2 steps or 3 steps at a time.
If the staircase has n steps, write a function to count the number of possible ways in which child can run up the stairs.

For e.g.

n == 1 then answer = 1

n == 3 then answer = 4

n == 5 then answer = 13

'''


def staircase(n):
    # Base Case - minimum steps possible and number of ways the child can climb them

    # Inductive Hypothesis - ways to climb rest of the steps

    # Inductive Step - use Inductive Hypothesis to formulate a solution
    memory = {}

    return helperFunction(n, memory)


def helperFunction(n, memory):

    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    sub3, sub2, sub1 = None, None, None
    try:
        index = n-3
        sub3 =  memory[index]
    except KeyError:
        sub3 = helperFunction(index, memory)
        memory[index] = sub3

    try:
        index = n-2
        sub2 =  memory[index]
    except KeyError:
        sub2 = helperFunction(index, memory)
        memory[index] = sub2

    try:
        index = n-1
        sub1 =  memory[index]
    except KeyError:
        sub1 = helperFunction(index, memory)
        memory[index] = sub1


    result = sub1 + sub2 + sub3
    memory[n] = result

    return result

print(staircase(4))
print(staircase(5))
print(staircase(20))



