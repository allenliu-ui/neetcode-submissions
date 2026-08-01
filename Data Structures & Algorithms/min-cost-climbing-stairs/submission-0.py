class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        minCost = float('inf')
        return min(self.memo(0, cache, minCost, cost), self.memo(1, cache, minCost, cost))
    def memo(self, i, cache, minCost, cost):
        if i in cache:
            return cache[i]

        if i >= len(cost):
            return 0
        cost1 = self.memo(i + 1, cache, minCost, cost)
        cost2 = self.memo(i + 2, cache, minCost, cost)
        result = cost[i] + min(self.memo(i + 1, cache, minCost, cost), self.memo(i + 2, cache, minCost, cost))
        cache[i] = result
        return result        
