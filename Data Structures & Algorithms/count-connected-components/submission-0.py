class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        components = n
        def find(x):
            p = parent[x]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        for a, b in edges:
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pa] = pb
                components -= 1
        return components