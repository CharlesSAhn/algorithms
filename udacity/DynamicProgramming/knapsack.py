'''
The items, each having its associated weight (kg) and value ( $ ).
A knapsack that can hold a maximum weight of knapsack_max_weight (kg).
Use dynamic programming to implement the function knapsack_max_value() to return the maximum total value of items that can be accommodated into the given knapsack.

Note - The items variable is the type Item, which is a named tuple.
'''

# Helper code
import collections

# An item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])


# Get the maximum total value ($) of items that can be accommodated into the given knapsack
def knapsack_max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    # Initialize a lookup table to store the maximum value ($)
    lookup_table = [0] * (knapsack_max_weight + 1)

    # Iterate down the given list
    for item in items:

        # The "capcacity" represents amount of remaining capacity (kg) of knapsack at a given moment.
        for capacity in reversed(range(knapsack_max_weight + 1)):

            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]




#print(knapsack_max_value(15, [Item(10, 7), Item(9, 8), Item(5, 6)]))

print(knapsack_max_value(5, [Item(1, 7), Item(2, 8), Item(3, 6)]))