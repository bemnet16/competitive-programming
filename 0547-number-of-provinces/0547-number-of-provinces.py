class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = [False for _ in range(len(isConnected))]
        
        def dfs(node):
            
            visited[node] = True
            
            for neighbour in range(len(isConnected[node])):
                if not visited[neighbour] and isConnected[node][neighbour]:
                    dfs(neighbour)
        
        
        count = 0
        for node in range(len(isConnected)):
            if not visited[node]:
                count += 1
                dfs(node)
                
        return count
                
        