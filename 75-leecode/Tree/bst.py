
class Node:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:

  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = Node(value)

    if self.root is None:
      self.root = new_node
      return

    current = self.root

    while True:
      if value == current.value:
        return

      if value <= current.value:
        if current.left is None:
          current.left = new_node
          return
        current = current.left
      else:
        if current.right is None:
          current.right = new_node
          return
        current = current.right

  def search(self, value):
    current = self.root

    while current is not None:
      if value == current.value:
        return True

      elif value <= current.value:
        current = current.left
      else:
        current = current.right

    return False

  def delete(self, value):
    if self.root is None:
      return False

    current = self.root
    parent = None

    while current is not None:
      if value == current.value:
        break
      elif value <= current.value:
        parent = current
        current = current.left
      else:
        parent = current
        current = current.right
    
    if current is None:
      return False

    if current.left is None and current.right is None:

      if current == self.root:
        self.root = None
      elif current == parent.left:
        parent.left = current.left
      else:
        parent.right =current.left
    
    elif current.left is not None and current.right is None:
      if current == self.root:
        self.root = current.left
      elif current == parent.left:
        parent.left = current.left
      else:
        parent.right = current.left 


    elif current.left is None and current.right is not None:
      if current = self.root:
        self.root = current.right 
      elif current == parent.left:
        parent.left = current.right
      else:
        parent.right = current.right

    else:
        parent = current
        successor = current.right
        while successor.left is not None:
          parent = successor
          successor = successor.left

        current.value = successor.value
        if parent.left == successor:
          parent.left = successor.right
        else:
          parent.right = successor.right

    return True



      