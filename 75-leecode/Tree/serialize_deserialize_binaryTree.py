'''

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    res = []

    def dfs(node, res):

        if node is None:
            res.append("null")

            return

        res.append(str(node.val))

        dfs(node.left, res)
        dfs(node.right, res)

        return


    dfs(root, res)

    return ",".join(res)




def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """

    vals = data.split(",")
    i = 0

    def dfs():
        nonlocal i
        if vals[i] == "null":
            i += 1
            return None

        node = TreeNode(int(vals[i]))

        i += 1
        node.left = dfs()
        node.right = dfs()

        return node

    return dfs()






node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.right = TreeNode(3)
node1.right.left = TreeNode(4)
node1.right.right = TreeNode(5)

res = serialize(node1)
print(res)

print(deserialize(res))