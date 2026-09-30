from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq_map = Counter(nums)
        uniques = [num for num in freq_map.keys() if freq_map[num] == 1]
        return max(uniques) if uniques != [] else -1
        