'''Given the root of a binary tree, find the diameter.

Note: Diameter of a Binary Tree is the maximum distance between any two nodes

'''

class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# The function Compute the "height" of a tree. Height is the
# number of nodes along the longest path from the root node
# down to the farthest leaf node.

def height(node):

    if node is None:
        return 0

    return 1 + max(height(node.left), height(node.right))


def diameter_of_binary_tree_func(root):
    """
    Diameter for a particular BinaryTree Node will be:
        1. Either diameter of left subtree
        2. Or diameter of a right subtree
        3. Sum of left-height and right-height
    :param root:
    :return: [height, diameter]
    """

    if root is None:
        return 0,0

    left_height, left_diameter = diameter_of_binary_tree_func(root.left)
    right_height, right_diameter = diameter_of_binary_tree_func(root.right)

    current_height = max(left_height, right_height) + 1
    height_diameter = left_height + right_height
    current_diameter = max(left_diameter, right_diameter, height_diameter)

    return current_height, current_diameter


from queue import Queue

def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree
    ex .arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
    """
    index = 0
    length = len(arr)

    if length <= 0:
        return -1

    q = Queue()
    root = BinaryTreeNode(arr[index])
    index += 1
    q.put(root)

    while len(q) > 0:

        current_node = q.get()
        left_child = arr[index]
        index += 1

        if left_child is not None:
            node = BinaryTreeNode(left_child)
            current_node.left = node
            q.put(node)

        right_child = arr[index]
        index += 1

        if right_child is not None:
            node = BinaryTreeNode(right_child)
            current_node.right = node
            q.put(node)
    return root








