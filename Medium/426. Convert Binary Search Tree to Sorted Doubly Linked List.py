"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return root

        l = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            l.append(root)
            dfs(root.right)

        dfs(root)

        for i in range(len(l) - 1):
            l[i].right = l[i + 1]
            l[i + 1].left = l[i]

        l[-1].right = l[0]
        l[0].left = l[-1]

        return l[0]
