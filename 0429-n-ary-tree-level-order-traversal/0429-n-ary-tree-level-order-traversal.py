"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return
        
        
        level = [root]
        answer = []
        
        
        while level:
            
            level_answer = []
            next_level = []
            
            for node in level:
                
                level_answer.append(node.val)
                
                for child in node.children:
                    next_level.append(child)
            
            
            answer.append(level_answer)
            level = next_level
            
        
        return answer
        