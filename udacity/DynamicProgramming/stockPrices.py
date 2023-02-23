'''

You are given access to yesterday's stock prices for a single stock. The data is in the form of an array with the stock price in 30 minute intervals from 9:30 a.m EST opening to 4:00 p.m EST closing time.
With this data, write a function that returns the maximum profit obtainable. You will need to buy before you can sell.

For example, suppose you have the following prices:

prices = [3, 4, 7, 8, 6]

The Idea
The given array has the prices of a single stock at 13 different timestamps. The idea is to pick two timestamps:
 "buy_at_min" and "sell_at_max" such that the buy is made before a sell. We will use two pairs of indices while traversing the array:

Pair 1 - This pair keeps track of our maximum profit while iterating over the list. It is done by storing a pair of indices - min_price_index, and max_price_index.
Pair 2 - This pair keeps track of the profit between the lowest price seen so far and the current price while traversing the array. The lowest price seen so far is maintained with current_min_price_index.
At each step we will make the greedy choice by choosing prices such that our profit is maximum. We will store the maximum of either of the two profits mentioned above.

'''


def max_returns(prices):
    """
    Calculate maxiumum possible return

    Args:
       prices(array): array of prices
    Returns:
       int: The maximum profit possible
    """

    min_price_index = 0
    max_price_index = 1

    current_min_price_index = 0

    if len(prices) < 2:
        return

    for index in range(1, len(prices)):

        if prices[index] < prices[current_min_price_index]:
            current_min_price_index = index

        # current max profit
        if prices[max_price_index] - prices[min_price_index] < prices[index] - prices[current_min_price_index]:
            max_price_index = index
            min_price_index = current_min_price_index

    max_price = prices[max_price_index] - prices[min_price_index]

    return max_price



    return prices


prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]

print(max_returns(prices))