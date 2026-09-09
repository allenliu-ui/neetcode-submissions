class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Counter = Counter(s1)
        windowCount = Counter(s2[:len(s1)])
        if windowCount == s1Counter:
            return True
        for i in range(len(s1), len(s2)):
            windowCount[s2[i]] += 1
            left_char = s2[i - len(s1)]
            windowCount[left_char] -= 1
            if windowCount[left_char] == 0:
                del windowCount[left_char]
            if windowCount == s1Counter:
                return True
        return False

        