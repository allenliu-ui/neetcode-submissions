class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i):
            if i == len(nums):
                res.append(nums.copy())
                return
            for j in range(i, len(nums)):
                if j > i and nums[i] == nums[j]:
                    continue
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)
            for k in range(len(nums) - 1, i, -1):
                nums[k], nums[i] = nums[i], nums[k]
    
        nums.sort()
        dfs(0)
        return res