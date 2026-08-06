class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for dst, src in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            for nextCourse in adj[course]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)
        return res if len(res) == numCourses else []