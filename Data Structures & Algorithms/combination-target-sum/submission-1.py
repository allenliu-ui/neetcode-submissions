class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        self.helper(0, combs, [], 0, target, nums)
        return combs

    def helper(self, i, combs, currCombs, total, target, nums):
        if total == target:
            combs.append(currCombs.copy())
            return
        if i >= len(nums) or total > target:
            return
        currCombs.append(nums[i])
        self.helper(i, combs, currCombs, total + nums[i], target, nums)
        currCombs.pop()
        self.helper(i + 1, combs, currCombs, total, target, nums)