# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        level = [root]
        answer = []
        
        
        while level:
            
            level_sum = 0.0
            next_level = []
            
            for node in level:
                
                level_sum += node.val
                
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
            
            
            level_average = (level_sum / len(level))
            answer.append(level_average)
            
            level = next_level
        
        
        return answer
                    
        