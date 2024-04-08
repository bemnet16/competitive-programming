class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        answer = [-1] * n
        graph = defaultdict(set)
        
        for node, edge in redEdges:
            graph[node].add((edge, "red"))
        
        for node, edge in blueEdges:
            graph[node].add((edge, "blue"))
        
        
        level = [(0, None)]
        visited = set((0, None))
        length = 1
        
        
        while level:
            
            next_level = []
            
            for node, p_col in level:
                if (node, p_col) in visited:
                    continue
                
                visited.add((node, p_col))
                
                for edge, col in graph[node]:
                    
                    if (p_col == None or p_col != col):
                        if answer[edge] == -1:
                            answer[edge] = length
                        else:
                            answer[edge] = min(answer[edge], length)
                        next_level.append((edge, col))
                        
            length += 1
            level = next_level
            
        answer[0] = 0
        return answer
                
                
            
            