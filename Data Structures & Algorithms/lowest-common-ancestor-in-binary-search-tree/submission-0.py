# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        right = None
        left = None
        if root == p or root == q:
            return root
        if root.left is not None:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right is not None:
            right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            return root
        elif right is not None:
            return right
        else:
            return left

