class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def recursion(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False
            if s[i] == t[j]:
                return recursion(i + 1, j + 1)
            return recursion(i, j + 1)
        return recursion(0, 0)