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

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

        return

    def remove(self, value):

        if self.head is None:
            return None

        ## if the value is head
        if self.head.value == value:
            self.head == None
            return None

        node = self.head

        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return None

            node = node.next

        return None

    # pop the first node
    def pop(self):

        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value

        return None


    def insert(self, position, value):

        if position < 0:
            return None

        if position == 0:
            self.prepend(value)
            return None

        node = self.head
        index = 1
        while node.next:
            if position == index:
                temp = Node(value)
                temp.next = node.next
                node.next = temp

                return
            index += 1
            node = node.next

        return None

    def returnSize(self):

        counter = 0
        node = self.head

        while node:
            counter += 1
            node = node.next

        return counter

    def to_list(self):
        res = []
        node = self.head
        while node:
            res.append(node.value)
            node = node.next

        return res


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

node = linked_list.head
while node:
    print(node.value)
    node = node.next

print(linked_list.to_list())