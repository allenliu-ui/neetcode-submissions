class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        translation1 = {}
        translation2 = {}
        for i in range(len(s)):
            if (s[i] in translation1 and translation1[s[i]] != t[i]) or (t[i] in translation2 and translation2[t[i]] != s[i]):
                return False
            translation1[s[i]] = t[i]
            translation2[t[i]] = s[i]
        return True