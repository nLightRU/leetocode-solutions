# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Пока не работает
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def add_sum(s, node):
            if node.val >= low and node.val <= high:
                s += node.val
            if node.left:
                s += add_sum(s, node.left)
            elif node.right:
                s += add_sum(s, node.right)
            else:
                return s

        result_sum = 0
        result_sum += add_sum(result_sum, root)
        return result_sum