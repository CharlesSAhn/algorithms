'''

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree

'''




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        counter = 0
        stack = []

        node = root

        while len(stack) > 0 and node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            print(node.val)
            counter += 1

            if counter == k:
                return node.val

            node = node.right