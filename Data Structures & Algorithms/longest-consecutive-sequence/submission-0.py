class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        increments = set(nums)
        longest = 0
        for num in increments:
            if num - 1 not in increments:
                length = 1
                while (num + length) in increments:
                    length += 1
                longest = max(length, longest)
        return longest