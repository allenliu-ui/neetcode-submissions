class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def traverse(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            area = 1
            for dr, dc in directions:
                area += traverse(row + dr, col + dc)
            return area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islandArea = traverse(i, j)
                    maxArea = max(maxArea, islandArea)
        return maxArea
