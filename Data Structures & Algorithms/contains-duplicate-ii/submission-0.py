class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        vals = set()
        L = 0
        for R in range(len(nums)):
            if abs(L - R) > k:
                vals.remove(nums[L])
                L += 1
            if nums[R] in vals:
                return True
            vals.add(nums[R])
        return False