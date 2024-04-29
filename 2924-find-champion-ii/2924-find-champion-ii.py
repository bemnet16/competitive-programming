class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        inDegree = [0] * n
        graph = defaultdict(set)
        
        for u, v in edges:
            inDegree[u] += 1
            graph[v].add(u)
        
        
        noni = []
        queue = deque()
        
        for i, deg in enumerate(inDegree):
            if deg == 0:
                queue.append(i)
        
        
        while queue:
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                
                if not graph[node]:
                    noni.append(node)
                    continue
                
                for nei in graph[node]:
                    
                    inDegree[nei] -= 1
                    
                    if inDegree[nei] == 0:
                        queue.append(nei)
        
        if len(noni) == 1:
            return noni[0]
        return -1
        