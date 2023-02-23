'''

Given the root of a binary tree, invert the tree, and return its root.

'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertTree(root):

    if root is None:
        return

    left = invertTree(root.left)
    right = invertTree(root.right)

    root.left = right
    root.right = left

    return root


root = TreeNode(4)
node2 = TreeNode(2)
node7 = TreeNode(7)
node1 = TreeNode(1)
node3 = TreeNode(3)
node6 = TreeNode(6)
node9 = TreeNode(9)

root.left = node2
root.right = node7
node2.left = node1
node2.right = node3
node7.left = node6
node7.right = node9

print(invertTree(root))