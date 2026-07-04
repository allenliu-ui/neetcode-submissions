class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        def memoization(r, c, row, col, cache):
            if r == row or c == col or obstacleGrid[r][c] == 1:
                return 0
            if r == row - 1 and c == col - 1:
                return 1
            if cache[r][c] > 0:
                return cache[r][c]
            cache[r][c] = memoization(r + 1, c, row, col, cache) + memoization(r, c+1, row, col, cache)
            return cache[r][c]
        return memoization(0, 0, row, col, [[0] * col for i in range(row)])