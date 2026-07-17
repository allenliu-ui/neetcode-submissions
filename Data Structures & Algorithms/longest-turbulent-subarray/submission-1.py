class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L, R = 0, 1
        res = 1
        prev_symbol = ""
        while R < len(arr):
            if arr[R - 1] > arr[R] and prev_symbol != ">":
                res = max(res, R - L + 1) 
                R += 1
                prev_symbol = ">"
            elif arr[R - 1] < arr[R] and prev_symbol != "<":
                res = max(res, R - L + 1)
                R += 1
                prev_symbol = "<"
            else:
                if arr[R - 1] == arr[R]:
                    L = R
                else:
                    L = R - 1
                R = L + 1
                prev_symbol = ""
        return res