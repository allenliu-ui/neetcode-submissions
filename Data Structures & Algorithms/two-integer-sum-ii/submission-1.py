class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            numSum = numbers[l] + numbers[r]
            if numSum == target:
                return [1 + l, 1 + r]
            if numSum > target:
                r -= 1
            else:
                l += 1
            