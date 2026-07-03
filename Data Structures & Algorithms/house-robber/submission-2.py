class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        i = 0
        while i < len(nums):
            temp = max(nums[i] + prev, curr)
            prev = curr
            curr = temp
            i += 1
        return curr