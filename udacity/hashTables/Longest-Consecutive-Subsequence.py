'''
Given list of integers that contain numbers in random order, write a program to find the longest possible sub sequence of
consecutive numbers in the array. Return this subsequence in sorted order. The solution must take O(n) time

For e.g. given the list 5, 4, 7, 10, 1, 3, 55, 2, the output should be 1, 2, 3, 4, 5

Note- If two arrays are of equal length return the array whose index of smallest element comes first.
'''

import copy

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def longest_consecutive_subsequence(input_list):
    # TODO: Write longest consecutive subsequence solution

    # iterate over the list and store element in a suitable data structure
    head = Node(input_list[0])
    node = head
    for i in range(1, len(input_list)):

        previous = None
        insert = False
        while node:
            if input_list[i] < node.data:
                if previous is None:
                    head = Node(input_list[i])
                    head.next = node
                else:
                    temp = previous.next
                    previous.next = Node(input_list[i])
                    previous.next.next = temp
                insert = True
                break
            previous = node
            node = node.next

        if insert is False:
            previous.next = Node(input_list[i])
        node = head


    current_max = 0
    counter = 0

    start_index = 0
    end_index = 0

    map = dict()
    sorted_data_list = list()

    node = head
    while node.next:

        if node.data + 1  == node.next.data:
            counter += 1
        else:
            current_max = max(current_max, counter)
            map[counter] = (start_index, end_index)
            start_index = end_index + 1
            counter = 0

        end_index += 1
        sorted_data_list.append(node.data)
        node = node.next

    print(sorted_data_list)
    start_index = map[current_max][0]
    end_index = map[current_max][1]
    return sorted_data_list[start_index:end_index+1]



    # traverse / go over the data structure in a reasonable order to determine the solution


print(longest_consecutive_subsequence([ 5, 4, 7, 10, 1, 3, 55, 2,8,9,11,12, 99]))