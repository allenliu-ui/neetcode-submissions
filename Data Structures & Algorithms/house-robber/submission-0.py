class Solution:
    def rob(self, nums: List[int]) -> int:
        maxMoney = {}
        for i in range(len(nums)):
            if i == 0:
                maxMoney[i] = nums[0]
            elif i == 1:
                maxMoney[i] = max(nums[0], nums[1])
            else:
                maxMoney[i] = max(nums[i] + maxMoney[i-2], maxMoney[i-1])
        return maxMoney[len(nums) - 1]
