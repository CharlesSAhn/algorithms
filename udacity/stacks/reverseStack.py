'''
Reverse a stack. If your stack initially has 1, 2, 3, 4 (4 at the top and 1 at the bottom),
 after reversing the order must be 4, 3, 2, 1 (4 at the bottom and 1 at the top).
'''

class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def reverse_stack(stack):
    """
    Reverse a given input stack

    Args:
       stack(stack): Input stack to be reversed
    Returns:
       stack: Reversed Stack
    """
    holder_stack = Stack()

    while stack.size() > 0:
        holder_stack.push(stack.pop())

    restore_stock(stack, holder_stack)


def restore_stock(originalStack, tempStack):

    if tempStack.is_empty():
        return

    data = tempStack.pop()

    restore_stock(originalStack, tempStack)

    originalStack.push(data)
    # return originalStack



test_case = [1, 2, 3, 4,6,7]

stack = Stack()
for num in test_case:
    stack.push(num)

reverse_stack(stack)

while not stack.is_empty():
    data = stack.pop()
    print(data)