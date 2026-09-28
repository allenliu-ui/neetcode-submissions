"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mappings = {None: None}
        curr = head
        while curr:
            mappings[curr] = Node(curr.val)
            curr = curr.next
        curr2 = head
        while curr2:
            copy = mappings[curr2]
            copy.next = mappings[curr2.next]
            copy.random = mappings[curr2.random]
            curr2 = curr2.next
        return mappings[head]
        