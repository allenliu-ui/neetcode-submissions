# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def treeValid(lower, upper, root):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return treeValid(lower, root.val, root.left) and treeValid(root.val, upper, root.right)
        return treeValid(-float('inf'), float('inf'), root)