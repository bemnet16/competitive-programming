from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return
        
        answer = deque()
        level = [root]
        
        while level:
            
            next_level = []
            level_answer = []
            
            for node in level:
                
                level_answer.append(node.val)
                
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
                    
            answer.appendleft(level_answer)
            level = next_level
        
        
        return answer
            
        
        