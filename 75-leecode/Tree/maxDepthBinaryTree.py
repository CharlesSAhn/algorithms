'''

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def maxDepth(node):

    if node is None:
        return 0

    left = maxDepth(node.left)
    right = maxDepth(node.right)

    return max(left, right) + 1



node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node5.left = node6

print(maxDepth(node1))