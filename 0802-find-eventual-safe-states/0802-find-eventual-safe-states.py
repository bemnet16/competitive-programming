from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        outDegree = [0] * len(graph)
        newGraph = defaultdict(set)
        
        for node in range(len(graph)):
            
            outDegree[node] = len(graph[node])
            for neighbour in graph[node]:
                newGraph[neighbour].add(node)
                
                
                
        queue = deque()
        visited = set()
        
        for node, degree in enumerate(outDegree):
            if degree == 0:
                queue.append(node)
        
        
        
        answer = []
        
        while queue:
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                answer.append(node)
                
                for neighbour in newGraph[node]:
                    
                    if neighbour not in visited:
                        
                        if outDegree[neighbour] == 1:
                            queue.append(neighbour)
                            visited.add(neighbour)
                            outDegree[neighbour] = 0
                            
                        else:
                            outDegree[neighbour] -= 1
        
        
        
        
        return sorted(answer)
                
                
