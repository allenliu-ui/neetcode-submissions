class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        for char in t:
            if char in counts:
                counts[char] -= 1
            else:
                return False
        for value in counts.values():
            if value != 0:
                return False
        return True