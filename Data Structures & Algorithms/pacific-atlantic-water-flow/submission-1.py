class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        visited = set()
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])
        def dfs(r, c, visited, prev_height):
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or heights[r][c] < prev_height:
                return 
            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pacific, -float('inf'))
        for r in range(rows):
            dfs(r, 0, pacific, -float('inf'))
        for c in range(cols):
            dfs(rows - 1, c, atlantic, -float('inf'))
        for r in range(rows):
            dfs(r, cols - 1, atlantic, -float('inf'))
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append((r, c))
        return res
        