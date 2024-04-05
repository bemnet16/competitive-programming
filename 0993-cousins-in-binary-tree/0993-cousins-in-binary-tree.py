# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        level = [root]
        
        while level:
            
            next_level = []
            oneFound = False
            
            for node in level:
                
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x):
                        return False
                
                if (node.val == x or node.val == y) and oneFound:
                     return True
                
                elif node.val == x or node.val == y:
                    oneFound = True
                    
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
            
            if oneFound:
                return False
            
            level = next_level
    
        return False
                
            