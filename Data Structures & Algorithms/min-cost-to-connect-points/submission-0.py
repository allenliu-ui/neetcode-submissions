class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        for i in range(len(points)):
            adj[i] = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([weight, j])
                adj[j].append([weight, i])
        res = 0
        visit = set()
        minHeap = [[0, 0]]
        while len(visit) < len(points):
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for newCost, new in adj[i]:
                if new not in visit:
                    heapq.heappush(minHeap, [newCost, new])
        return res