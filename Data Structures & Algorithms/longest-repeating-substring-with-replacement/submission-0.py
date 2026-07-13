class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        length = 0
        chars = {}
        max_f = 0
        for R in range(len(s)):
            chars[s[R]] = 1 + chars.get(s[R], 0)
            max_f = max(max_f, chars[s[R]])
            if (R - L + 1) - max_f > k:
                chars[s[L]] -= 1
                L += 1
            length = max(length, R - L + 1)
        return length