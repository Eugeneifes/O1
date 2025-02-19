# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Самый длинный путь между двумя узлами бинарного дерева состоит из 3-х элементов:
- некоторого узла
- его самой длинной левой части
- его самой длинной правой части

Таким образом, чтобы найти самый длинный путь (диаметр) - нужно сравнить между собой все такие пути в дереве
Для обхода дерева будем использовать поиск в глубину (Depth-first Search или DFS)
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path(node):
            if not node:
                return 0

            nonlocal diameter
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            diameter = max(diameter, left_path + right_path)

            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter