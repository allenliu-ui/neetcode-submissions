class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = {0}

        for stone in stones:
            new_dp = set(dp)
            for current_sum in dp:
                new_sum = current_sum + stone
                if new_sum <= target:
                    new_dp.add(new_sum)
            dp = new_dp
        max_sum = max(dp)
        return (total - max_sum) - max_sum