# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        GRAPH = defaultdict(set)
        
        nodes = [root]
        
        while nodes:
            
            next_nodes = []
            
            for node in nodes:
                
                if node.left:
                    GRAPH[node.val].add(node.left.val)
                    GRAPH[node.left.val].add(node.val)
                    next_nodes.append(node.left)
                
                if node.right:
                    GRAPH[node.val].add(node.right.val)
                    GRAPH[node.right.val].add(node.val)
                    next_nodes.append(node.right)
            
            nodes = next_nodes
        
        
        
        def bfs(start):
            
            nodes = [start]
            visited = {start}
            times = -1
            
            while nodes:
                
                next_nodes = []
                
                for node in nodes:
                    
                    for neigh in GRAPH[node]:
                        if neigh not in visited:
                            visited.add(neigh)
                            next_nodes.append(neigh)
                
                times += 1
                nodes = next_nodes
            
            return times
        
        
        
        return bfs(start)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            