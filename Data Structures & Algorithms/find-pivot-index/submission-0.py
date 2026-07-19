class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        indexes = []
        total = 0
        for num in nums:
            total += num
            indexes.append(total)
        for i in range(len(nums)):
            leftSum = indexes[i - 1] if i > 0 else 0 
            rightSum = indexes[-1] - indexes[i]
            if leftSum == rightSum:
                return i
        return -1