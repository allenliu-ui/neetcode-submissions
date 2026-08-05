class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            key = tuple(count)
            if key in dictionary:
                dictionary[key].append(word)
            else:
                dictionary[key] = [word]
        return list(dictionary.values())
        