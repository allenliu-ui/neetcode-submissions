class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {num : i for i, num in enumerate(nums)}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in indexes and indexes[complement] != i:
                return [i, indexes[complement]]