class Solution:
    def spiralOrder(self, a: List[List[int]]) -> List[int]:
        dir = [0, 1]; cur = [0, 0]
        d = {(0, 1): [1, 0], (1, 0): [0, -1], (0, -1): [-1, 0], (-1, 0): [0, 1]}
        n = len(a); m = len(a[0])
        seen = [[False for _ in range(m)] for _ in range(n)]
        def check():
            nxt = [cur[0]+dir[0], cur[1]+dir[1]]; return nxt[0] >= 0 and nxt[0] < n and nxt[1] >= 0 and nxt[1] < m and seen[nxt[0]][nxt[1]] is False
        ans = []
        while sum([sum(r) for r in seen]) < n*m:
            ans.append(a[cur[0]][cur[1]]); seen[cur[0]][cur[1]] = True
            if not check():
                dir = d[(dir[0], dir[1])]
            cur[0] += dir[0]; cur[1] += dir[1];
        return ans
        