class Node(object):

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None



class Tree():

    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root










