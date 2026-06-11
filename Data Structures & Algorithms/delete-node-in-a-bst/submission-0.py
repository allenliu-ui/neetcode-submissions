# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        curr = root
        if curr.val < key:
            root.right = self.deleteNode(root.right, key)
        elif curr.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            new_Node = root.right
            while new_Node.left:
                new_Node = new_Node.left
            new_Node.left = root.left
            return root.right
        return root
    
