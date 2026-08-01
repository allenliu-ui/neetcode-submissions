class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        return min(self.memo(0, cache,cost), self.memo(1, cache, cost))
    def memo(self, i, cache, cost):
        if i in cache:
            return cache[i]

        if i >= len(cost):
            return 0
        cost1 = self.memo(i + 1, cache, cost)
        cost2 = self.memo(i + 2, cache, cost)
        result = cost[i] + min(cost1, cost2)
        cache[i] = result
        return result        
