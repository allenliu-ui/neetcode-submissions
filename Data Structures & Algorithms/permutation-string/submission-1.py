class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts = Counter(s1)
        counts2 = Counter(s2[:len(s1)])
        if counts2 == counts:
            return True
        for i in range(len(s1), len(s2)):
            counts2[s2[i]] += 1
            left_char = s2[i -len(s1)]
            counts2[left_char] -= 1
            if counts2[left_char] == 0:
                del counts2[left_char]
            if counts2 == counts:
                return True
        return False