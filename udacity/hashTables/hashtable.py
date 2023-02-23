'''
In this quiz, you'll write your own hash table and hash function that uses string keys. Your table will store strings in buckets by their first two letters, according to the formula below:

Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter

You can assume that the string will have at least two letters, and the first two characters are uppercase letters
(ASCII values from 65 to 90). You can use the Python function ord() to get the ASCII value of a letter, and chr() to get the letter associated with an ASCII value.

You'll create a HashTable class, methods to store and lookup values, and a helper function to calculate a hash value given a string.
You cannot use a Python dictionary—only lists! And remember to store lists at each bucket, and not just the string itself.
For example, you can store "UDACITY" at index 8568 as ["UDACITY"].
'''

"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class LinkedList():

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """TODO: Input a string that's stored in
        the table."""

        hash_value = self.calculate_hash_value(string)

        #check if the index has any value

        node = self.table[hash_value]

        while node:
            if node.key == hash_value:
                node.value = string
                return

        new_node = LinkedList(hash_value, string)

        new_node.next = self.table[hash_value]
        self.table[hash_value] = new_node

        return


    def lookup(self, string):
        """TODO: Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""

        hash_value = self.calculate_hash_value(string)

        node = self.table[hash_value]
        while node:
            if node.key == hash_value:
                return node.value

        return -1

    def calculate_hash_value(self, string):
        """TODO: Helper function to calulate a
        hash value from a string."""

        hash_value = ord(string[0]) * 100 + ord(string[1])

        return hash_value


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print (hash_table.calculate_hash_value('UDACITY'))
# Test lookup edge case
# Should be -1
print (hash_table.lookup('UDACITY'))
# Test store
hash_table.store('UDACITY')
print (hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print (hash_table.lookup('UDACIOUS'))