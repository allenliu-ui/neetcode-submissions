class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i <= max_reach:
                max_reach = max(max_reach, i + nums[i])
            if i > max_reach:
                return False
            if i == len(nums) - 1:
                return True
        return max_reach >= len(nums) - 1
