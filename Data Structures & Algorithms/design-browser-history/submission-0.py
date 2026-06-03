class ListNode:
    def __init__(self, str="", next=None, prev=None):
        self.str = str
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = LinkedList()
        homepageNode = ListNode(homepage, self.history.tail, self.history.head)
        self.history.head.next = homepageNode
        self.history.tail.prev = homepageNode
        self.marker = homepageNode

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.marker.next = newNode
        newNode.next = self.history.tail
        newNode.prev = self.marker
        self.history.tail.prev = newNode
        self.marker = self.marker.next

    def back(self, steps: int) -> str:
        while (steps > 0 and self.marker.prev != self.history.head):
            self.marker = self.marker.prev
            steps -= 1
        return self.marker.str
        
    def forward(self, steps: int) -> str:
        while (steps > 0 and self.marker.next != self.history.tail):
            self.marker = self.marker.next
            steps -= 1
        return self.marker.str


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)