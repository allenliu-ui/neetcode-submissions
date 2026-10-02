# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = dummy = ListNode()
        curr1 = list1
        curr2 = list2
        while (curr1 != None) and (curr2 != None):
            if curr1.val <= curr2.val:
                dummy.next = curr1
                curr1 = curr1.next
                dummy = dummy.next
            else:
                dummy.next = curr2
                curr2 = curr2.next
                dummy = dummy.next
        dummy.next = curr1 or curr2
        return node.next
