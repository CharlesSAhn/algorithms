from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self,value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"



class Node():

	def __init__(self, value):
		self.value = value
		self.right = None 
		self.left = None 



class BST():

	def __init__(self):

		self.root = None 

	def insert(self, value):
		
		new_node = Node(value)

		if not self.root:
			self.root = new_node 
			return

		node = self.root
		while True:

			if value == node.value:
				return

			elif value < node.value:
				if node.left:
					node = node.left
				else:
					node.left = new_node 
					break 
			else:
				if node.right:
					node =  node.right 
				else:
					node.right = new_node
					break

		return

	def insert_recursively(self, value):

		return __insert_recursively(self, self.root, value)

	def __insert_recursively(self, node, value):

		if node is None:
			return Node(value)

		if node.value > value:
			node.left = self.__insert_recursively(ndoe.left, value)
		else:
			node.right = self.__insert_recursively(node.right, value)

		return node 


	def delete(self, value):
		'''
		case 1: No children:  just delete
		case 2: single children: copy that child to that node
		case 3: if two children:  determine the next highest element (inorder successor) in the right subtree. 
		Replace the node to be removed withte inorder sucessor.  Delete the inorder successor duplicate. 
		'''
		return self.__delete_node__(self.root, value)

	def __delete_node__(self, node, value):

		if not node:
			return None 

		if value < node.value: 
			node.left = self.__delete_node__(node.left, value)

		elif value > node.value:
			node.right = self.__delete_node__(node.right, value)

		else:
			# If the node is with only one child or no child
			if node.left is None:
				tmp = node.right 
				node = None 
				return tmp 

			elif node.right is None: 
				tmp = node.left 
				node = None 
				return tmp  

			# if node has two children
			# place the inorder successor in position of the node to be deleted.

			temp = self.minValueNode(node.right) 

			node.value = temp.value 

			node.right = self.__delete_node__(node.right, temp.value)

		return node

	def minValueNode(self, node):

		while node.left:
			node =  node.left 

		return node 


	def search(self, value):
		
		node = self.root 

		while True:

			if node.value == value:
				return True

			elif value < node.value:
				if node.left:
					node = node.left
				else:
					return False 
			else:
				if node.right:
					node = node.right 
				else:
					return False 

	def __repr__(self):
		level = 0
		q = Queue()
		visit_order = list()
		node = self.root
		q.enq( (node,level) )
		while(len(q) > 0):
			node, level = q.deq()
			if node == None:
				visit_order.append( ("<empty>", level))
				continue
			visit_order.append( (node, level) )
			if node.left:
				q.enq( (node.left, level +1 ))
			else:
				q.enq( (None, level +1) )

			if node.right:
				q.enq( (node.right, level +1 ))
			else:
				q.enq( (None, level +1) )

		s = "Tree\n"
		previous_level = -1
		for i in range(len(visit_order)):
			node, level = visit_order[i]
			if level == previous_level:
				if node == "<empty>":
					s += " | " + str(node)
				else:
					s += " | " + str(node.value)
			else:
				if node == "<empty>":
					s += "\n" + str(node)
				else:
					s += " | " + str(node.value)
				previous_level = level
		return s



bstTree = BST()
bstTree.insert(8)
bstTree.insert(3)
bstTree.insert(1)
bstTree.insert(6)
bstTree.insert(7)
bstTree.insert(10)
bstTree.insert(4)
print(bstTree)

print(bstTree.search(1))
print(bstTree.search(100))

bstTree.delete(4)
print(bstTree)

bstTree.delete(6)
print(bstTree)

bstTree.delete(3)
print(bstTree)
