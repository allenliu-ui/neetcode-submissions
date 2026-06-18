import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stoneOne = heapq.heappop(stones)
            stoneTwo = heapq.heappop(stones)
            heapq.heappush(stones, stoneOne - stoneTwo)
        return -stones[0]