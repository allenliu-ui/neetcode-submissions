from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        pairings = defaultdict(set)
        for word1, word2 in similarPairs:
            pairings[word1].add(word2)
            pairings[word2].add(word1)
        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i] and sentence2[i] not in pairings.get(sentence1[i], set()):
                return False
        return True 