'''

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

'''
import collections


class TreeNode:

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None



def levelOrder(root):

    result = collections.defaultdict(list)

    level = 0
    queue = [(level, root)]

    while len(queue) > 0:

        item = queue.pop(0)

        if item[1] is not None:
            result[item[0]].append(item[1].val)

            queue.append((item[0]+1, item[1].left))
            queue.append((item[0]+1, item[1].right))

    return result.values()





