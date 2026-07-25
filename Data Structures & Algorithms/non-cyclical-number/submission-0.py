class Solution:
    def isHappy(self, n: int) -> bool:
        values = set()
        while n != 1 and n not in values:
            values.add(n)
            n = self.sumSquare(n)
        return n == 1
    def sumSquare(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n //= 10
        return output