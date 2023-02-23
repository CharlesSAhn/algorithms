'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''


def start_climb(n):

    cache = [None for _ in range(n)]
    return climb(n, cache)


def climb(n, cache):

    if n == 1:
        return 1

    if n == 2:
        return 2

    if cache[n-1] is None:
        cache[n-1] = climb(n-1, cache)

    if cache[n-2] is None:
        cache[n-2] = climb(n-2, cache)

    return cache[n-1] + cache[n-2]


print(start_climb(3))
print(start_climb(5))