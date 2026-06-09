class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles) 
        while left <= right:
            speed = (left + right) // 2
            if self.eatingSpeed(piles, h, speed):
                right = speed - 1
            else:
                left = speed + 1
        return left



    def eatingSpeed(self, piles, h, k):
        total = 0
        for pile in piles:
            total += (pile + k - 1) // k
        if total <= h:
            return True
        return False