class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(L, R, s):
            res = ""
            while L >= 0 and R < len(s) and s[L] == s[R]:
                res = s[L] + res + s[R] if L != R else s[L]
                L -= 1
                R += 1
            return res
        
        maxString = ""
        for i in range(len(s)):
            odd = expand(i, i, s)
            even = expand(i, i + 1, s)
            maxString = max(maxString, even, odd, key=len)
        return maxString

