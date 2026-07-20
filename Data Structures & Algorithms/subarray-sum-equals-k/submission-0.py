class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curSum = 0
        mapVal = {0: 1}
        for num in nums:
            curSum += num
            diff = curSum - k
            count += mapVal.get(diff, 0)
            mapVal[curSum] = mapVal.get(curSum, 0) + 1
        return count