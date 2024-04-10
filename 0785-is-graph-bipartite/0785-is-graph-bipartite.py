class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        colors = ["white" for _ in range(len(graph))]
        visited = set()
        
        
        def dfs(node):
            
            visited.add(node)
            for neighbour in graph[node]:
                
                if colors[node] == colors[neighbour]:
                    return False
                
                if colors[neighbour] == "white":
                    if colors[node] == "blue":
                        colors[neighbour] = "red"
                    else:
                        colors[neighbour] = "blue"
                
                if neighbour not in visited:
                    dfs(neighbour)
            
            return True
        
        for i, color in enumerate(colors):
            if color == "white":
                colors[i] = "blue"
            if not dfs(i):
                return False
            
        return True