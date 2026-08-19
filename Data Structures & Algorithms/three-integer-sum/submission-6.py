class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            a = nums[i]
            if i > 0 and a == nums[i - 1]:
                continue
            if a > 0:
                break
            target = -a
            L, R = i + 1, len(nums) - 1
            while L < R:
                currSum = nums[L] + nums[R]
                if currSum == target:
                    res.append([a, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
                elif currSum < target:
                    L += 1
                else:
                    R -= 1
        return res
