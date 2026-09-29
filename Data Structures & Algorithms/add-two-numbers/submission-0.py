# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        head = ListNode()
        curr = head
        while l1 or l2 or carry:
            num1 = 0 if l1 is None else l1.val
            num2 = 0 if l2 is None else l2.val
            numRes = num1 + num2 + 1 if carry == True else num1 + num2
            if numRes > 9:
                carry = True
                numRes = numRes % 10
            else:
                carry = False
            curr.val = numRes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2 or carry:
                curr.next = ListNode()
                curr = curr.next
        return head
