'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

'''

class Node():

    def __init__(self, data):

        self.data = data
        self.next = None


def detectCycle(head):

    slow = head
    fast= head

    # if head is None:
    #     return False
    #
    # if fasterpointer is None:
    #     return False

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True


    return False


head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(detectCycle(head))