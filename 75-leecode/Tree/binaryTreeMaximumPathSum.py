'''

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root):

    current_max = [root.val]

    def recursive(treeNode):

        if treeNode is None:
            return 0

        leftmax = recursive(treeNode.left)
        rightmax = recursive(treeNode.right)

        leftmax = max(leftmax, 0)
        rightmax = max(rightmax, 0)

        current_max[0] = max(current_max[0], leftmax + rightmax + treeNode.val)


        return treeNode.val + max(leftmax , rightmax)

    recursive(root)

    return current_max[0]



