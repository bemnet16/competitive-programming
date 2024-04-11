# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        nodes = [root]
        path_track = defaultdict(TreeNode)
        path_track[root] = TreeNode(-1)
        
        while nodes:
            
            next_nodes = []
            
            for node in nodes:
                
                if node == target:
                    break
                    
                if node.left:
                    path_track[node.left] = node
                    next_nodes.append(node.left)
                
                if node.right:
                    path_track[node.right] = node
                    next_nodes.append(node.right)
                    
                    
            nodes = next_nodes
        
        
        path = []
        cur_node = target
        
        while cur_node in path_track:
            path.append(cur_node)
            cur_node = path_track[cur_node]
        
        
        def bfs(root, dis):
            
            if dis < 0:
                return []
            
            level = [root]
            
            for _ in range(dis):
                
                next_level = []
                
                for node in level:
                    
                    if node.left:
                        next_level.append(node.left)
                    
                    if node.right:
                        next_level.append(node.right)
                
                level = next_level
            
            return [node.val for node in level]
        
        
        
        answer = []
        for idx, node in enumerate(path):
            
            if idx - k == 0:
                answer.append(node.val)
                continue
            
            if idx == 0:
                answer.extend(bfs(node, (k - idx)))
            
            else:
                if node.left == path[idx - 1] and node.right:
                    answer.extend(bfs(node.right, (k - idx - 1)))
                
                elif node.right == path[idx - 1] and node.left:
                    answer.extend(bfs(node.left, (k - idx - 1)))
            
        
        
        return answer
        
        
