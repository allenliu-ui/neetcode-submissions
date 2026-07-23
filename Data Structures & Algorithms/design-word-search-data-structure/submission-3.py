class WordNode:
    def __init__(self):
        self.characters = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.characters:
                curr.characters[c] = WordNode()
            curr = curr.characters[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            curr = node
            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    for child in curr.characters.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.characters:
                        return False
                    curr = curr.characters[char]
            return curr.is_end
        return dfs(0, self.root)
        
