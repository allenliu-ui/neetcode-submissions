class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(nums):
            prev_2 = 0
            prev_1 = 0
            for money in nums:
                current = max(prev_2 + money, prev_1)
                prev_2 = prev_1
                prev_1 = current
            return prev_1
        if len(nums) == 1:
            return nums[0]
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
