class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for src, dst in prerequisites:
            adj[src].append(dst)
        visit = set()
        toposort = []
        res = []
        for i in range(numCourses):
            self.dfs(i, adj, toposort, visit)
        toposort.reverse()

        isPrereq = [set() for i in range(numCourses)]
        for node in toposort:
            for neighbor in adj[node]:
                isPrereq[neighbor].add(node)
                isPrereq[neighbor].update(isPrereq[node])
        for u, v in queries:
            res.append(u in isPrereq[v])
        return res
            
    
    def dfs(self, src, adj, toposort, visit):
        if src in visit:
            return True
        visit.add(src)

        for neighbor in adj[src]:
            self.dfs(neighbor, adj, toposort, visit)
        toposort.append(src)
        
        
