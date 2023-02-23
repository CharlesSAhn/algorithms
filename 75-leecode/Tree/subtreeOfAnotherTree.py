'''

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False

        if self.isSameTree(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))




    def isSameTree(self, node, node2):

        if node is None and node2 is None:
            return True

        if node is None or node2 is None:
            return False

        if node.val != node2.val:
            return False

        return (self.isSameTree(node.left, node2.left) and self.isSameTree(node.right, node2.right))

