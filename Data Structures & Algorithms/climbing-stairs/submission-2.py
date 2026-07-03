class Solution:
    def climbStairs(self, n: int) -> int:
        def tracker(n, cache):
            if n <= 2:
                return n
            if n in cache:
                return cache[n]
            cache[n] = tracker(n-1, cache) + tracker(n-2, cache)
            return cache[n]
        return tracker(n, {})
