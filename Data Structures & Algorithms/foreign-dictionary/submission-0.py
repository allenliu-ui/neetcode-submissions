class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        visited = set()
        res = []
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""
            minLen = min(len(w1), len(w2))
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        def dfs(node, in_progress, graph, res, visited):
            if node in in_progress:
                return ""
            if node in visited:
                return None
            in_progress.append(node)
            for neighbor in graph[node]:
                result = dfs(neighbor, in_progress, graph, res, visited)
                if result == "":
                    return ""
            in_progress.remove(node)
            visited.add(node)
            res.append(node)
            return None
        for char in adj:
            if char not in visited:
                if dfs(char, [], adj, res, visited) == "":
                    return ""
        res.reverse()
        return "".join(res)



            