class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        translation1 = {}
        translation2 = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            keyChar = pattern[i]
            keyWord = words[i]
            if (keyChar in translation1 and translation1[keyChar] != keyWord) or (keyWord in translation2 and translation2[keyWord] != keyChar):
                return False
            translation1[keyChar] = keyWord
            translation2[keyWord] = keyChar
        return True

