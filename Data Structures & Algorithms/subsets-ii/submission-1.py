class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset, curSets = [], []
        self.helper2(0, nums, subset, curSets)
        return subset
    
    def helper2(self, i, nums, subsets, curSets):
        if i >= len(nums):
            subsets.append(curSets.copy())
            return
        curSets.append(nums[i])
        self.helper2(i + 1, nums, subsets, curSets)
        curSets.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper2(i + 1, nums, subsets, curSets)