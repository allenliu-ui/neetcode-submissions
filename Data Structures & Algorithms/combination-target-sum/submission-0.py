class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, val):
            if val == target:
                res.append(subset.copy())
                return
            if val > target or i == len(nums):
                return
            subset.append(nums[i])
            dfs(i, val + nums[i])
            subset.pop()
            dfs(i + 1, val)
        dfs(0, 0)
        return res