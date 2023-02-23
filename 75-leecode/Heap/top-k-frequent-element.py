'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]

'''

from collections import defaultdict


class Heap():

    def __init__(self, initial_size = 10):

        self.heap_list = [None for _ in range(initial_size)]
        self.next_index = 0

    def insert(self, data):

        #insert data
        self.heap_list[self.next_index] = data

        self.up_heapify()

        self.next_index += 1

        if self.next_index == len(self.heap_list):
            temp  = self.heap_list

            self.heap_list = [None for _ in range(self.next_index * 2)]

            for index, num in enumerate(self.temp):
                self.heap_list[index] = num

        return

    def up_heapify(self):

        '''

        [0,1,2,3,4,5,6,7]
             0
           1  2
        3  4 5 6
       7

       left_child = parent * 2 + 1
       right_child = parent * 2 + 2

       parent = (left_child -1 ) // 2
       parent = (right_child - 2) // 2

        '''

        child_index = self.next_index

        while child_index > 0:

            parent_index = (child_index - 1) // 2

            child_value = self.heap_list[child_index]
            parent_Value = self.heap_list[parent_index]

            if child_value[1] < parent_Value[1]:
                break
            else:
                self.heap_list[child_index] = parent_Value
                self.heap_list[parent_index] = child_value

                child_index = parent_index

    def remove(self):

        if len(self.heap_list) == 0:
            return

        self.next_index -= 1

        to_remove = self.heap_list[0]
        self.heap_list[0] = self.heap_list[self.next_index]
        self.heap_list[self.next_index] = None

        self.down_heapify()

        return to_remove



    def down_heapify(self):

        '''

        left_child = parent * 2 + 1
        right_child = parent * 2 + 2

        '''

        parent_index = 0

        while parent_index < len(self.heap_list):

            left_index = parent_index * 2 + 1
            right_index = parent_index * 2 + 2

            parent = self.heap_list[parent_index]
            left_child = None
            right_child = None

            max_child = parent

            if left_index < self.next_index:
                left_child = self.heap_list[left_index]

            if right_index < self.next_index:
                right_child = self.heap_list[right_index]

            if left_child is not None:
                if left_child[1] > max_child[1]:
                    max_child = left_child

            if right_child is not None:
                if right_child[1] > max_child[1]:
                    max_child = right_child

            if max_child == parent:
                return

            elif max_child == left_child:
                self.heap_list[parent_index] = left_child
                self.heap_list[left_index] = parent
                parent_index = left_index

            else:
                self.heap_list[parent_index] = right_child
                self.heap_list[right_index] = parent
                parent_index = right_index



def topKfrequent(nums, k):

    if k < 1:
        return []

    if len(nums) < k:
        return []

    stats = defaultdict(int)

    for num in nums:
        stats[num] += 1

    # heap sort [(number, frequency)]
    # sort based on frequency number

    heap = Heap()

    for key, value in stats.items():
        heap.insert((key, value))

    result = []

    for i in range(k):
        result.append(heap.remove()[0])

    return result

print(topKfrequent([1,1,1,2,2,3,1,2,3,2,2,2,2,2,2], 2))
print(topKfrequent([1,1,1,2,2,3], 2))
print(topKfrequent([1], 1))