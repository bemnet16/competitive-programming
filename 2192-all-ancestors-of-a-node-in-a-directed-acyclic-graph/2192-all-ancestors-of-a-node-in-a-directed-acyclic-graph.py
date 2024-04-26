from sortedcontainers import SortedSet
from collections import deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        degree = [0] * n
        graph = defaultdict(set)
        allAncestor = defaultdict(SortedSet)
        
        for from_i, to_i in edges:
            degree[to_i] += 1
            graph[from_i].add(to_i)
        
        
        queue = deque()
        
        for node, deg in enumerate(degree):
            if deg == 0:
                queue.append(node)
                degree[node] -= 1
        
        
        while queue:
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                
                for neighbour in graph[node]:
                    
                    degree[neighbour] -= 1
                    if degree[neighbour] == 0:
                        queue.append(neighbour)
                    
                    
                    if node not in allAncestor[neighbour]:
                        allAncestor[neighbour].add(node)
                        allAncestor[neighbour].update(allAncestor[node])
        
        
        
        answer = []
        
        for node in range(n):
            answer.append(allAncestor[node])
        
        
        return answer
                        
