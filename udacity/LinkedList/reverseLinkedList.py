
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        #move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])



def reverse(linked_list):

    new_list = LinkedList()
    node = linked_list.head
    prev_node = None

    for value in linked_list:
        new_node = Node(value)
        new_node.next = prev_node
        prev_node = new_node
    new_list.head = new_node

    return new_list

llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)
print(llist)
print(reverse(llist))