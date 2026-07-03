class Solution:
    def climbStairs(self, n: int) -> int:
        def tracker(n, cache):
            if n <= 2:
                return n
            prev, curr = 1, 2
            for i in range(3, n+1):
                prev, curr = curr, curr + prev
            return curr
        return tracker(n, {})
