'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


prices = [7,4,5,1,6,4]
'''


def maxProfit(input):

    res = 0

    if len(input) < 2:
        return res

    leftpointer = 0
    rightpointer = 1
    max = 0

    for i in range(0, len(input)-1):
        diff = input[rightpointer] - input[leftpointer]

        if diff < 0:
            leftpointer = rightpointer

        else:
            if diff > max:
                max = diff
        rightpointer += 1

    return max

print(maxProfit([7,1,5,3,6,4]))

print(maxProfit([7,4,5,1,6,4]))
