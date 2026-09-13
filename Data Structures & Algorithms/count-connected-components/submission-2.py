class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        
        adj={i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(i, prev):
            if i in visit:
                return
            visit.add(i)
            for j in adj[i]:
                # if j == prev:
                #     continue
                dfs(j, i)
            return
        
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i,-1)
                count += 1
        return count            