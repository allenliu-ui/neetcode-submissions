import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            closest.append((dist, point[0], point[1]))
        heapq.heapify(closest)
        result = []
        for i in range(k):
            closePoint = heapq.heappop(closest)
            result.append([closePoint[1], closePoint[2]])
        return result