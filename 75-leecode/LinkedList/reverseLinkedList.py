'''

Given the head of a singly linked list, reverse the list, and return the reversed list.

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseList(head):

    if head is None or head.next is None:
        return head

    current_node = head.next
    prev_node = head
    prev_node.next = None

    while current_node is not None:
        temp = current_node.next

        current_node.next = prev_node
        prev_node = current_node
        current_node = temp


    return prev_node






head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

reverseList(head)

