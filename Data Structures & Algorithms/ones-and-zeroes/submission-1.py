class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for i in range(m + 1)]
        counts = []
        for string in strs:
            countZero = string.count('0')
            countOne = string.count('1')
            counts.append((countZero, countOne))
        for zeroes, ones in counts:
            for i in range(m, zeroes - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeroes][j - ones])      
        return dp[m][n]
