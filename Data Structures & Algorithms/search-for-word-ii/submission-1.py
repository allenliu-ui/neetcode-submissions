class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        myTrie = TrieNode()
        res, visit = set(), set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        for word in words:
            myTrie.addWord(word)
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r, c) in visit or board[r][c] not in node.children):
                return 
            visit.add((r, c))
            char = board[r][c]
            node = node.children[board[r][c]]
            word += char
            if node.is_word:
                res.add(word)
            for dr, dc in directions:
                dfs(r + dr, c + dc, node, word)
            visit.remove((r, c))
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, myTrie, "") 
        return list(res)