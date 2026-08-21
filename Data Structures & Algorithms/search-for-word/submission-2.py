class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, x, y, grid, word, visit):

            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x, y) in visit or grid[x][y] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            visit.add((x, y))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            for newX, newY in directions:
                if dfs(i + 1, x + newX, y + newY, grid, word, visit):
                    return True
            visit.remove((x, y))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(0, i, j, board, word, set()):
                        return True
        return False           


    