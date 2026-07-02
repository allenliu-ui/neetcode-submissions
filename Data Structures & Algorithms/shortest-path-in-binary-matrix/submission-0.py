class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        if (grid[0][0] == 1):
            return -1
        queue.append((0,0))
        visit.add((0,0))
        length = 0
        while queue:
            length += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                if (r == ROW - 1 and c == COL - 1):
                    return length
                directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]]
                for dr, dc in directions:
                    if r+dr < 0 or c+dc < 0 or r+dr >= ROW or c+dc >= COL or grid[r+dr][c+dc] == 1 or (r+dr, c+dc) in visit:
                        continue
                    queue.append((r+dr, c+dc))
                    visit.add((r+dr, c+dc))
        return -1
        
