class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        degree = defaultdict(int)
        
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
        
        
        for k, v in degree.items():
            if v != 1:
                return k
        