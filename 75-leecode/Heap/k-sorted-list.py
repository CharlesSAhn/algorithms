'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6


Input: lists = []
Output: []

Input: lists = [[]]
Output: []

constraints:
- k == lists.length
- 0 <= k <= 104
- 0 <= lists[i].length <= 500
- -104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''

class Listnode:

    def __init__(self, value):
        self.value = value
        self.next = None


def mergeKList(input):

    heap = Heap(10)

    for linkedList in input:

        node = linkedList

        while node:
            heap.insert(node.value)
            node = node.next

    head = Listnode(heap.remove())

    while heap.size() > 0:
        node = Listnode(heap.remove())
        node.next = head

        head = node

    return head



class Heap:

    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]
        self.next_index = 0

    def insert(self, data):

        self.cbt[self.next_index] = data

        self.up_heapify()

        self.next_index += 1

        # check the list
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(len(self.cbt * 2))]

            for index in range(0, len(temp)):
                self.cbt[index] = temp[index]


    def up_heapify(self):

        '''

        p = parent
        left_child = p*2 +1
        right_child = p*2 + 2

        parent = (left_child - 1) / 2
        parent = (right_child -2) / 2
        '''

        child_index = self.next_index

        while child_index > 0:

            parent_index = (child_index - 1) // 2

            if self.cbt[parent_index] < self.cbt[child_index]:
                self.cbt[parent_index], self.cbt[child_index] = self.cbt[child_index], self.cbt[parent_index]

                child_index = parent_index

            else:
                break

    def remove(self):

        if len(self.cbt) == 0:
            return None

        self.next_index -= 1
        to_remove = self.cbt[0]
        self.cbt[0] = self.cbt[self.next_index]
        self.cbt[self.next_index] = None

        self.down_heapify()

        return to_remove


    def down_heapify(self):

        '''

        parent = p * 2 + 1
        parent = p * 2 + 2

        '''

        parent_index = 0

        while parent_index < len(self.cbt):

            left_child_index = parent_index * 2 + 1
            right_child_index = parent_index * 2 + 2

            left_child = None
            right_child = None
            parent = self.cbt[parent_index]

            max_child = parent

            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            if left_child is not None:
                max_child =  max(parent, left_child)

            if right_child is not None:
                max_child = max(max_child, right_child)

            if max_child == parent:
                return

            if max_child == left_child:
                self.cbt[parent_index] = max_child
                self.cbt[left_child_index] = parent
                parent_index = left_child_index
            else:
                self.cbt[parent_index] = max_child
                self.cbt[right_child_index] = parent
                parent_index = right_child_index


    def size(self):
        return self.next_index



listnode1 = Listnode(1)
listnode1.next = Listnode(2)
listnode1.next.next = Listnode(4)

listnode2 = Listnode(1)
listnode2.next = Listnode(5)
listnode2.next.next = Listnode(7)


listnode3 = Listnode(2)
listnode3.next = Listnode(6)
listnode3.next.next = Listnode(10)

result = mergeKList([listnode1, listnode2, listnode3])

while result:
    print(result.value)
    result = result.next