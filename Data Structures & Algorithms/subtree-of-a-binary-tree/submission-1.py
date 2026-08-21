# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def searchroot(root1, root2):
            res = None
            left = None
            right = None
            if root1:
                if root1.val == root2.val:
                    res = checkMatch(root1, root2)
                left = searchroot(root1.left, root2)
                right = searchroot(root1.right, root2)
            return res or left or right or False
        


        def checkMatch(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return checkMatch(root1.left, root2.left) and checkMatch(root1.right, root2.right)
        
        if not subRoot:
            return True
        return searchroot(root, subRoot)
            
        
        