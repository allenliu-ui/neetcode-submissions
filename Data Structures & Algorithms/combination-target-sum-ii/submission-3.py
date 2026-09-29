class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i == len(candidates):
                return
            curr.append(candidates[i])
            total += candidates[i]
            dfs(i + 1, curr, total)
            curr.pop()
            total -= candidates[i]
            val = candidates[i]
            i = i + 1
            while i < len(candidates) and candidates[i] == val:
                i += 1
            dfs(i, curr, total)
        dfs(0, [], 0)
        return res
            