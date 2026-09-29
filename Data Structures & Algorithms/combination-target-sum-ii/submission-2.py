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
            skip_i = i + 1
            while skip_i < len(candidates) and candidates[skip_i] == val:
                skip_i += 1
            dfs(skip_i, curr, total)
        dfs(0, [], 0)
        return res
            