# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_Node = TreeNode(val)
        if not root:
            return new_Node
        curr = root
        while True:
            if (curr.val > val):
                if curr.left is None:
                    curr.left = new_Node
                    break
                curr = curr.left
            elif (curr.val < val):
                if curr.right is None:
                    curr.right = new_Node
                    break
                curr = curr.right
        return root 