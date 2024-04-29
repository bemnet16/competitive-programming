class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        inDegree = [0] * n
        graph = defaultdict(set)
        
        for u, v in edges:
            inDegree[u] += 1
            graph[v].add(u)
        
        
        
        strongest = []
        queue = deque()
        
        for i, deg in enumerate(inDegree):
            if deg == 0:
                queue.append(i)
        
        
        
        while queue:
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                
                if not graph[node]:
                    strongest.append(node)
                    continue
                
                for neighbour in graph[node]:
                    
                    inDegree[neighbour] -= 1
                    
                    if inDegree[neighbour] == 0:
                        queue.append(neighbour)
        
        
        
        if len(strongest) == 1:
            return strongest[0]
        return -1
        