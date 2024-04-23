class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        
        visited = set()
        maxCycle = -1
        
        def dfs(node, vis, dis_track, dis):
            
            nonlocal maxCycle
            
            if edges[node] != -1:
                
                if edges[node] in visited:
                    if edges[node] in vis:
                        maxCycle = max(maxCycle, dis - dis_track[edges[node]] + 1)
                
                else:
                    visited.add(edges[node])
                    vis.add(edges[node])
                    dis += 1
                    dis_track[edges[node]] = dis
                    dfs(edges[node], vis, dis_track, dis)
        
        
        
        for node in range(len(edges)):
            
            if node not in visited:
                visited.add(node)
                dfs(node, {node}, {node: 0}, 0)
        
        
        return maxCycle