from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        path_track = defaultdict(int)
        answer = []
        
        def backtrack(node):
            
            queue = deque()
            while node != root:
                queue.appendleft(str(node.val))
                node = path_track[node]
            queue.appendleft(str(node.val))
            
            return "->".join(queue)
            
            
        
        cur_nodes = [root]
        
        while cur_nodes:
            
            next_nodes = []
            
            for node in cur_nodes:
                
                if not (node.left or node.right):
                    answer.append(backtrack(node))
                
                if node.left:
                    path_track[node.left] = node
                    next_nodes.append(node.left)
                
                if node.right:
                    path_track[node.right] = node
                    next_nodes.append(node.right)
            
            cur_nodes = next_nodes
        
        
        return answer
                
        