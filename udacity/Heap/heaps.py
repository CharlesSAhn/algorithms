

class Heap:

    def __init__(self, initial_size):

        self.cbt = [None for _ in range(initial_size)]
        self.next_index = 0


    def remove(self):

        if len(self.cbt) == 0:
            return

        self.next_index -= 1

        to_remove = self.cbt[0]
        self.cbt[0] = self.cbt[self.next_index]
        self.cbt[self.next_index] = None

        self.down_heapify()

        return to_remove

    def down_heapify(self):
        '''

        parent
        left_child = p*2 +1
        right_child = p* + 2
        '''

        parent_index = 0

        while parent_index < len(self.cbt):

            left_child_index = parent_index * 2 + 1
            right_child_index = parent_index * 2 + 2

            left_child = None
            right_child = None
            parent = self.cbt[parent_index]

            min_child = parent

            # if child index exist
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]


            if left_child is not None:
                min_child = min(parent, left_child)

            if right_child is not None:
                min_child = min(min_child, right_child)


            if min_child == parent:
                return

            if min_child == left_child:
                self.cbt[parent_index] = left_child
                self.cbt[left_child_index] = parent
                parent_index = left_child_index

            else:
                self.cbt[parent_index] = right_child
                self.cbt[right_child_index] = parent
                parent_index = right_child_index



    def insert(self, data):

        self.cbt[self.next_index] = data

        self.up_heapify()

        self.next_index += 1

        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(0, self.next_index):
                self.cbt[index] = temp[index]


    def up_heapify(self):

        '''

        parent
        left_child = p*2 +1
        right_child = p* + 2

        parent = (left_child - 1) / 2
        parent = (right_child -2) / 2
        '''

        child_index = self.next_index

        while child_index > 0:

            parent_index = (child_index - 1) // 2

            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if self.cbt[child_index] < self.cbt[parent_index]:
                self.cbt[child_index] = parent_element
                self.cbt[parent_index] = child_element

                child_index = parent_index

            else:
                break


    def size(self):
        return self.next_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]

    def is_empty(self):
        return self.size() == 0


heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)
print('Inserted elements: {}'.format(elements))

print('size of heap: {}'.format(heap.size()))

for _ in range(4):
    print('Call remove: {}'.format(heap.remove()))


print('Call get_minimum: {}'.format(heap.get_minimum()))

for _ in range(2):
    print('Call remove: {}'.format(heap.remove()))

print('size of heap: {}'.format(heap.size()))
print('Call remove: {}'.format(heap.remove()))
print('Call is_empty: {}'.format(heap.is_empty()))