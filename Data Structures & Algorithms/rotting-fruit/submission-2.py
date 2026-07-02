class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        totalMins = 0
        fresh = 0
        ROW, COL = len(grid), len(grid[0])
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        while fresh > 0 and queue:
            totalMins += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                directions = [[1,0],[-1,0],[0,-1],[0,1]]
                for dr, dc in directions:
                    if r+dr < 0 or c+dc < 0 or r+dr >= ROW or c+dc >= COL or grid[r+dr][c+dc] != 1:
                        continue
                    grid[r+dr][c+dc] = 2
                    queue.append((r+dr, c+dc))
                    fresh -= 1
        return totalMins if fresh == 0 else -1