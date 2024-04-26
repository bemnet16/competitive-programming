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
        
        for node, degree in enumerate(outDegree):
            if degree == 0:
                queue.append(node)
        
        
        
        answer = []
        
        while queue:
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                answer.append(node)
                
                for neighbour in newGraph[node]:
                        
                        outDegree[neighbour] -= 1
                        if outDegree[neighbour] == 0:
                            queue.append(neighbour)
                            
        
        return sorted(answer)
                
