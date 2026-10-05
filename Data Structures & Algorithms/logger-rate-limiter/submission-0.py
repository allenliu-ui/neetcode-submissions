class Logger:

    def __init__(self):
        self.apis = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.apis and timestamp - self.apis[message] < 10:
            return False    
        self.apis[message] = timestamp
        return True
            


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
