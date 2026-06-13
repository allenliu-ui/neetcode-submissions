# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def appendValues(root, arr):
            if not root:
                return None
            appendValues(root.left, arr)
            arr.append(root.val)
            appendValues(root.right, arr)
            return arr
        res = appendValues(root, [])
        return res
