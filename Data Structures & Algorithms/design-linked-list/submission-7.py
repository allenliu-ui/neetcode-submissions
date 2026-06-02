class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if (index < 0 or index >= self.size):
            return -1
        curr = self.head.next
        while (index > 0):
            curr = curr.next
            index -= 1
        return curr.val
        
    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        old_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = old_node
        old_node.prev = node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        old_node = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = old_node
        old_node.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if (index < 0 or index > self.size):
            return;
        curr = self.head.next
        node = ListNode(val)
        while (index > 1):
            curr = curr.next
            index -= 1
        old = curr.next
        curr.next = node
        node.prev = curr
        node.next = old
        old.prev = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if (index < 0 or index >= self.size):
            return;
        curr = self.head
        while (index > 0):
            curr = curr.next
            index -= 1
        deleted = curr.next
        curr.next = deleted.next
        deleted.next.prev = curr
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)