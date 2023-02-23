
class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def path_from_root_to_node(root, data):
    """
    :param: root - root of binary tree
    :param: data - value (representing a node)
    TODO: complete this method and return a list containing values of each node in the path
    from root to the data node
    """

    if root is None:
        return None

    if root.value == data:
        return [root.value]

    left_answer = path_from_root_to_node(root.left, data)

    if left_answer is not None:
        left_answer.append(root.value)
        return left_answer


    right_answer = path_from_root_to_node(root.right, data)

    if right_answer is not None:
        right_answer.append(root.value)
        return right_answer


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.left.left.left = BinaryTreeNode(7)


print(path_from_root_to_node(root,3))


