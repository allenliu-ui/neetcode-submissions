# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def countHeight(root, count):
            if not root:
                return 0
            else:
                return 1 + max(countHeight(root.left, count), countHeight(root.right, count))
        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)
        current_balanced = abs(countHeight(root.left, 0) - countHeight(root.right, 0)) < 2
        return left_balanced and right_balanced and current_balanced