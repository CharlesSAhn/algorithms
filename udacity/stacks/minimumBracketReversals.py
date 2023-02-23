'''

Given an input string consisting of only { and }, figure out the minimum number of reversals required to make the brackets balanced.

For example:

For input_string = "}}}}, the number of reversals required is 2.
For input_string = "}{}}, the number of reversals required is 1.

If the brackets cannot be balanced, return `-1` to indicate that it is not possible to balance them.

Approach:
- use stack
 - if empty:
      insert
   else:
      pop
        if pop == current char
           push char

- check the stack
     - pop next two stack:
            counter += 1
     if only one left:
        return -1
return counter
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head =  None
        self.size = 0

    def pop(self):

        if self.size == 0:
            return None

        data = self.head.value
        self.head = self.head.next
        self.size -= 1

        return data

    def push(self, value):

        if self.head is None:
            self.head = Node(value)

        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp

        self.size += 1
        return

    def length(self):
        return self.size

    def top(self):
        return self.head.value


def balanced_reversal(input):

    stack = Stack()
    for char in input:
        if stack.length() == 0:
            stack.push(char)
        else:

            if char == "{":
                stack.push(char)
            else:
                if stack.top() != char:
                    stack.pop()
                else:
                    stack.push(char)


    if stack.length() % 2 == 1:
        return -1
    else:
        counter = 0
        while stack.length() > 0:
            first = stack.pop()
            second = stack.pop()

            if first == second:
                counter += 1
            else:
                counter += 2

        return counter

print(balanced_reversal("}}}}"))
print(balanced_reversal("}}{{"))
print(balanced_reversal("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}"))
print(balanced_reversal("}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{"))
print(balanced_reversal("}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}"))