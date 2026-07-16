class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        maxVol = 0
        while L < R:
            currVol = (R - L) * min(heights[L], heights[R])
            maxVol = max(maxVol, currVol)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return maxVol