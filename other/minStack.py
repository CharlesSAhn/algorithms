

class Stack:

	def __init__(self):

		self.stack = []

	def push(self, value):
		if self.stack:
			self.stack.append((value, min(value, self.stack[-1][1])))
		else:
			self.stack.append((value, value))

	def pop(self):
		return self.stack.pop()[0]

	def getMin(self):

		return self.stack[-1][1]



s = Stack()
s.push(2)
s.push(4)
print(s.getMin())
s.push(1)
print(s.getMin())
