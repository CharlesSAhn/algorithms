'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_linkedlist(head1, head2):


    dummyNode = Node(0)

    tail = dummyNode

    while True:

        if head1 is None:
            tail.next = head2
            break

        if head2 is None:
            tail.next = head1
            break

        if head1.value < head2.value:
            tail.next = head1
            head1 = head1.next

        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next

    return dummyNode.next



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)

node1.next = node3
node3.next = node5
node5.next = node7

node2.next = node4


result = merge_linkedlist(node1, node2)