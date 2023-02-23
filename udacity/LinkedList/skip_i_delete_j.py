'''
You are given the head of a linked list and two integers, i and j. You have to retain the first i nodes and then delete the next j nodes. Continue doing so until the end of the linked list.

Example:

linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
i = 2
j = 3
Output = 1 2 6 7 11 12

Assumption:
- i and j will be valid number, something less than the size of the linked list.

'''

class Node():

    def __init__(self, value):
        self.value = value
        self.next = None


def modifylist(head, i, j):

    if head is None or i < 0 or j < 0:
        return None

    pointer = None
    i_counter = 1
    j_counter = 1

    node = head

    while i_counter < i and node.next:
        node = node.next
        i_counter += 1

    pointer = node

    while j_counter < j + 1 and node.next:
        node = node.next
        j_counter += 1

    pointer.next = node.next

    return head



# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.value, end=' ')
        head = head.next
    print()


arr = [1, 2, 3, 4, 5]
i = 2
j = 4

head = create_linked_list(arr)

print_linked_list(head)
head2 = modifylist(head, i, j)
print_linked_list(head2)
