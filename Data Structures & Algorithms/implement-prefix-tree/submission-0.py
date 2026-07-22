class PrefixNode:
    def __init__(self):
        self.characters = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.characters:
                curr.characters[c] = PrefixNode()
            curr = curr.characters[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.characters:
                return False
            curr = curr.characters[c]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.characters:
                return False
            curr = curr.characters[c]
        return True
        