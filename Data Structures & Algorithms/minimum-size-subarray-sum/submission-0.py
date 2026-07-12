class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        arr = 0
        L = 0
        for R in range(len(nums)):
            arr += nums[R]
            while arr >= target:
                length = min(R- L+ 1, length)
                arr -= nums[L]
                L += 1
        return 0 if length == float('inf') else length