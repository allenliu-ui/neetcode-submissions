class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.helper(1, [], combs, n, k)
        return combs

    def helper(self, i, curComb, combs, n, k):
        if len(curComb) == k:
            combs.append(curComb.copy())
            return
        if i > n:
            return
        for j in range(i, n + 1):
            curComb.append(j)
            self.helper(j + 1, curComb, combs, n, k)
            curComb.pop()