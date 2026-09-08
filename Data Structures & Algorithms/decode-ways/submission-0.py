class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n+1)]

        dp[0] = 1
        for i in range(n):
            c = s[i]
            
            if c != '0':
                dp[i+1] = dp[i]
            
            if i > 0:
                c = int(s[i-1] + s[i])
                if s[i-1] != '0' and 1 <= c and c <= 26:
                    dp[i+1] += dp[i-1]
        return dp[n]
        
