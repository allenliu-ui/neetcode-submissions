class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in indexes:
                return [indexes[complement], i]
            indexes[nums[i]] = i