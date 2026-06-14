# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        level = 0
        if root:
            queue.append(root)
        while len(queue) > 0:
            listLevel = []
            for i in range(0, len(queue)):
                node = queue.popleft()
                listLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(listLevel)
        return res
            

        