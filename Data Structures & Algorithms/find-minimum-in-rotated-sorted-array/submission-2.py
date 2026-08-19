class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        L, R = 0, len(nums) - 1
        while L < R:
            mid = L + (R - L) // 2
            if nums[mid] > nums[R]:
                L = mid + 1
                res = min(res, nums[mid])
            else:
                R = mid - 1
                res = min(res, nums[mid])
        return min(res, nums[L])
            

