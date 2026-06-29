class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROW, COL = len(grid), len(grid[0])
        islands = 0
        def traverse(row, col):
            if (row < 0 or col < 0 or row >= ROW or col >= COL or grid[row][col] == "0"):
                return 
            grid[row][col] = "0"
            for dr, dc in directions:
                traverse(row + dr, col + dc)
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    traverse(r, c)
                    islands += 1
        return islands