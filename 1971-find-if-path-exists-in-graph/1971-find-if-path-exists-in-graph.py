class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        GRAPH = defaultdict(set)
        
        for node, edge in edges:
            GRAPH[node].add(edge)
            GRAPH[edge].add(node)
        
        print(GRAPH)
        visited = set()
        
        def dfs(src):
            if src == destination:
                return True
            
            visited.add(src)
            for neighbor in GRAPH[src]:
                if neighbor not in visited:
                    result = dfs(neighbor)
                    
                    if result:
                        return True
            
        
        
        return dfs(source)