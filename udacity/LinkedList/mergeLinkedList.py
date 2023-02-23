
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

def merge(list1, list2):
    merged = LinkedList(None)

    if list1 is None:
        return list2
    if list2 is None:
        return list1

    node1 = list1.head
    node2 = list2.head

    while  node1 is not None or node2 is not None:

        if node1 is None:
            merged.append(node2.value)
            node2 = node2.next
        elif node2 is None:
            merged.append(node1.value)
            node1 = node1.next
        else:
            if node1.value > node2.value:
                merged.append(node2.value)
                node2 = node2.next
            else:
                merged.append(node1.value)
                node1 = node1.next

    return merged





linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)


merged = merge(linked_list, second_linked_list)
node = merged.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next


# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next