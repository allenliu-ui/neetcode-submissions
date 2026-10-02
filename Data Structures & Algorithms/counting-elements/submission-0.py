class Solution:
    def countElements(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            if arr[i] + 1 in arr:
                res += 1
        return res