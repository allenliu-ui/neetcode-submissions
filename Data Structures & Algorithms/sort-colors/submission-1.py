class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for num in nums:
            counts[num] += 1
        i = 0
        for k in range(0, len(counts)):
            for j in range(0, counts[k]):
                nums[i] = k
                i += 1
        