class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        edges = defaultdict(set)
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                cost = abs(x1 - x2) + abs(y1 - y2)
                
                edges[i].add((cost, j))
                edges[j].add((cost, i))
                
        
        
        ans = 0
        visited = set()
        heap = [(0, 0)]
        
        while len(visited) < n:
            
            cost, i = heappop(heap)
            if i in visited:
                continue
            ans += cost
            visited.add(i)
            for n_cost, nei in edges[i]:
                if nei not in visited:
                    heappush(heap, (n_cost, nei))
        
        
        return ans
            
                
                
        
        