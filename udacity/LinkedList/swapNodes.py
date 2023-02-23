'''
Given a linked list, swap the two nodes present at position i and j. The positions are based on 0-based indexing.

Note: You have to swap the nodes and not just the values.

Example:

linked_list = 3 4 5 2 6 1 9
positions = 3 4
output = 3 4 5 6 2 1 9
Explanation:

The node at position 3 has the value 2
The node at position 4 has the value 6
Swapping these nodes will result in a final order of nodes of 3 4 5 6 2 1 9


'''

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def swapnodes(head, left_index, right_index):

    if head is None or left_index < 0 or right_index < 0:
        return

    if left_index >= right_index:
        return

    node = head
    index_counter = 0

    left_prev = None
    left_node = None
    right_prev = None
    right_node = None


    for i in range(0, right_index + 1):

        if index_counter == left_index:
            left_node = node

        if index_counter == right_index:
            right_node = node

        if left_node is None:
            left_prev = node
        elif right_node is None:
            right_prev = node

        node = node.next
        index_counter += 1

    if left_index == 0:
        left_prev = left_node

    # when left node is first node
    if left_prev == left_node:
        head = right_node

    else:
        left_prev.next = right_node

    right_next_node = right_node.next

    if left_node != right_prev:
        left_next_node = left_node.next
        right_node.next = left_next_node
        right_prev.next = left_node
    else:
        right_node.next = left_node


    left_node.next = right_next_node


    return head


def create_linedlist(arr):

    if len(arr) <= 0:
        return

    head = Node(arr[0])

    tail = head

    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next

    return head


def print_linkedlist(head):

    node = head

    while node:
        print(node.data, end=" ")
        node = node.next
    print()


arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 1
right_index = 3
head = create_linedlist(arr)


print_linkedlist(head)

head2 = swapnodes(head, left_index, right_index)


print_linkedlist(head2)