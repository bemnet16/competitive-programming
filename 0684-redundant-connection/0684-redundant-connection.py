class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return True
            
            if rank[x] > rank[y]:
                parent[root_y] = root_x
            
            elif rank[x] < rank[y]:
                parent[root_x] = root_y
            
            else:
                parent[root_y] = root_x
                rank[root_x] += rank[root_y]
        
        
        for x, y in edges:
            if union(x, y):
                return [x, y]
            
            
        