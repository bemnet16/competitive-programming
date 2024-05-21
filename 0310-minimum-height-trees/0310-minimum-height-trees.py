class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if not edges: return [0]
        
        degree = defaultdict(int)
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            
            degree[a] += 1
            degree[b] += 1
        
        
        que = deque()
        for node in graph:
            if len(graph[node]) == 1:
                que.append(node)
        
        
        while que:
            if n <= 2:
                return que
            
            for _ in range(len(que)):
            
                node = que.popleft()
                n -= 1
                
                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        que.append(nei)