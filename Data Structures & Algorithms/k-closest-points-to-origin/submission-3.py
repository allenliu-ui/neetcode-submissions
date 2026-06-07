import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(closest, (-dist, point[0], point[1]))
            if len(closest) > k:
                maxPoint = heapq.heappop(closest)
        result = []
        for tupleDist in closest:
            result.append([tupleDist[1], tupleDist[2]])
        return result

        