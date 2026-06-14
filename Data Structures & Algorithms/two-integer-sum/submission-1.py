class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapIndex = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in mapIndex:
                res = [mapIndex[diff], i]
                return res
            mapIndex[nums[i]] = i