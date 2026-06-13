# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return (True, 0)
            left_balance, left_height = helper(root.left)
            right_balance, right_height = helper(root.right)
            curr = left_balance and right_balance and abs(left_height - right_height) < 2
            currHeight = 1 + max(left_height, right_height)
            return (curr, currHeight)

        balanced, height = helper(root)
        return balanced