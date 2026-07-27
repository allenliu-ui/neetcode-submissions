class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(range(len(profits)))
        projects.sort(key=lambda i: capital[i])
        profit_heap = []
        project_index = 0
        for i in range(k):
            while project_index < len(profits) and capital[projects[project_index]] <= w:
                heapq.heappush(profit_heap, -profits[projects[project_index]])
                project_index += 1
            if not profit_heap:
                break
            w += -heapq.heappop(profit_heap)
        return w