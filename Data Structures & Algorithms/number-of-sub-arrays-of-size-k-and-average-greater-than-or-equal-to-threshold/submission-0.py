class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        L = 0
        avg = 0
        for R in range(len(arr)):
            avg += arr[R]
            if abs(L - R) + 1 > k:
                avg -= arr[L]
                L += 1
            if abs(L - R) + 1 == k:
                if avg / k >= threshold:
                    count += 1
        return count
            