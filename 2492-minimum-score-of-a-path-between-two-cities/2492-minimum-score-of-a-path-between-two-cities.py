class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        
        for node1, node2, dis in roads:
            graph[node1].add((node2, dis))
            graph[node2].add((node1, dis))
        
        
        queue = deque([1])
        visited = {1}
        answer = float(inf)
        
        while queue:
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                
                for neighbour, distance in graph[node]:
                    
                    answer = min(answer, distance)
                    
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
                    
        
        
        return answer