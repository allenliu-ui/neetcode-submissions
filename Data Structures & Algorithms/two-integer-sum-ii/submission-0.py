class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 1, len(numbers)
        while L < R:
            if numbers[L - 1] + numbers[R - 1] == target:
                return [L, R]
            elif numbers[L - 1] + numbers[R - 1] < target:
                L += 1
            else:
                R -= 1
        return res