class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        maxEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= maxEnd:
                maxEnd = end
            else:
                count += 1
                maxEnd = min(maxEnd, end)
        return count