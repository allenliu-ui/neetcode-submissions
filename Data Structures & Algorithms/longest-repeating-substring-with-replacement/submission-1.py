class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0;
        l = 0;
        chars = {}
        max_f = 0;
        for r in range(len(s)):
            chars[s[r]] = 1 + chars.get(s[r], 0)
            max_f = max(max_f, chars[s[r]])
            if (r - l + 1) - max_f > k:
                chars[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)
        return length
            