class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLeft, minRight = 0, float('inf')
        L, R = 0, 0
        counts = {}
        windowCounts = {}
        matched = 0
        for char in t:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        while R < len(s):
            if s[R] in counts:
                if s[R] in windowCounts:
                    windowCounts[s[R]] += 1   
                else:
                    windowCounts[s[R]] = 1
                if windowCounts[s[R]] == counts[s[R]]:
                    matched += 1
            R += 1
            while matched == len(counts.keys()):
                if R - L < minRight - minLeft:
                    minLeft, minRight = L, R
                if s[L] in windowCounts:
                    windowCounts[s[L]] -= 1
                    if windowCounts[s[L]] < counts[s[L]]:
                        matched -= 1
                L += 1
        return s[minLeft:minRight] if minRight != float('inf') else ""