'''

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0


Approach:
- recursive loop thorugh the coins and resurive call (target - coin)

'''

import math

def coinChangeStart(coins, amount):

    cache = {}

    return coinChange(coins, amount, cache)

def coinChange(coins, amount, cache):

    current_min = -1

    if amount == 0:
        return 0

    for coin in coins:

        total = amount - coin

        if total == 0:
            return 1

        elif total < 0:
            return -1

        else:

            if total in cache:
                res = cache[total]
            else:
                res = coinChange(coins, total, cache)
                cache[total] = res + 1

            if res == -1:
                continue

            if current_min == -1:
                current_min = res + 1
            else:
                current_min = min(res + 1, current_min)

    return current_min


print(coinChangeStart([1,2,5], 11))
print(coinChangeStart([1], 11))
print(coinChangeStart([2], 3))
print(coinChangeStart([1], 0))

# coinChange([1,2,5], 11)
# coinChange([1,2,5], 6)   +@
# coinChange([1,2,5], 1)  + 1
# return 0
