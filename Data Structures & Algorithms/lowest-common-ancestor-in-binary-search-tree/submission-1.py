# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        minNode = min(p.val, q.val)
        maxNode = max(p.val, q.val)
        def search(node):
            if minNode < node.val < maxNode or node.val == minNode or node.val == maxNode:
                return node
            if node.val > minNode and node.val > maxNode:
                return search(node.left)
            else:
                return search(node.right)
        return search(root)
            
                