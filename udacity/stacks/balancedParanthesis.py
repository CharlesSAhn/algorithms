'''
In this exercise you are going to apply what you learned about stacks with a real world problem.
We will be using stacks to make sure the parentheses are balanced in mathematical expressions such as:
((32+8)∗(5/2))/(2+6).
In real life you can see this extend to many things such as text editor plugins and interactive development environments
for all sorts of bracket completion checks.

Take a string as an input and return True if it's parentheses are balanced or False if it is not.

'''

class Stack():

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):

        if self.size() == 0:
            return None

        else:
            return self.items.pop()


def checkBalance(input):

    if len(input) == 0:
        return True

    s = Stack()

    for char in input:
        if char == "(":
            s.push(char)
        elif char == ")":
            stack_top = s.pop()

            if stack_top is None:
                return False

    if s.size() > 0:
        return False

    return True


print(checkBalance('((3^2 + 8)*(5/2))/(2+6)'))
print(checkBalance('((3^2 + 8)*(5/2))/(2+6))'))
print(checkBalance('(((3^2 + 8)*(5/2))/(2+6)'))