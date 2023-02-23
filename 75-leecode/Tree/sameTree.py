'''

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

'''


class TreeNode:

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def dfs(tree, tree2):

    if tree is None and tree2 is None:
        return True


    if (tree is None and tree2 is not None) or (tree is not None and tree2 is None):
        return False


    if tree.val != tree2.val:
        return False

    return dfs(tree.left, tree2.left) and dfs(tree.right, tree2.right)


def isSameTree(tree1, tree2):

    return dfs(tree1, tree2)







tree1 = TreeNode(1)
tree2 = TreeNode(2)
tree3 = TreeNode(3)
tree4 = TreeNode(4)

tree1.left = tree2
tree1.right = tree3
tree2.left = tree4


tree1_1 = TreeNode(1)
tree2_2 = TreeNode(2)
tree3_3 = TreeNode(3)
tree4_4 = TreeNode(4)
tree5_5 = TreeNode(5)

tree1_1.left = tree2_2
tree1_1.right = tree3_3
tree2_2.left = tree4_4
#tree2_2.right = tree5_5

print(isSameTree(tree1, tree1_1))