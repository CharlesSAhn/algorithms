

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



def print_nodes(head):

    current_node = head
    while current_node:
        print(current_node.value)
        current_node = current_node.next


head = Node(2)
head.next = Node(1)

print_nodes(head)


def create_linked_list(input_list):
    head = None

    for value in input_list:
        if head is None:
            head = Node(value)

        else:
            current_node = head
            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(value)
    return head


def create_linked_list_better(input):

    head = None
    tail = None

    for value in input:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next

    return head
