'''
Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers.
Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.

Example:

linked list = 1 2 3 4 5 6
output = 1 3 5 2 4 6

Approach:
- create a second pointer and create a second chain
- at the end, link the second chain to first chain tail.

'''

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def udpateNode(head):

    node = head

    oddpointer = None
    oddTailPointer = None
    evenpointer = None
    eventTailPointer = None

    if head is None:
        return

    while node:

        #check for even or add
        if node.value % 2 == 0:
            if evenpointer is None:
                evenpointer = node
                eventTailPointer = node
            else:
                evenpointer.next = node
                eventTailPointer = eventTailPointer.next


        else:
            if oddpointer is None:
                oddpointer = node
                oddTailPointer = node
            else:
                oddTailPointer.next = node
                oddTailPointer = oddTailPointer.next


        node = node.next

    oddTailPointer.next = evenpointer
    eventTailPointer.next = None

    if oddpointer is None:
        return evenpointer

    return oddpointer


## 1 -> 2 -> 3 -> 4
# 1. oddpointer = 1   oddTailPointer = 1   oddTailPointer.next = 1   evenpointer = None    eventTailPointer = None
# 2. oddpointer = 1   oddTailPointer = 1   oddTailPointer.next = 1   evenpointer = 2       eventTailPointer = 2     eventTailPointer.next = 2
# 3. oddpointer = 1   oddTailPointer = 3   oddTailPointer.next = 3   evenpointer = 2       eventTailPointer = 2     eventTailPointer.next = 2

