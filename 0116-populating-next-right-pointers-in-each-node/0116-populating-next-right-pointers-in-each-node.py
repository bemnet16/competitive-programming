"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        queue = [root] if root else None
        
        while queue:
            
            nx_que = []
            
            for i in range(len(queue)):
                
                cur_node = queue[i]
                if i + 1 < len(queue):
                    cur_node.next = queue[i + 1]
                
                if cur_node.left:
                    nx_que.append(cur_node.left)
                    nx_que.append(cur_node.right)
                
            
            if nx_que:
                queue = nx_que
            else:
                queue = []
            
            
        return root
        
        