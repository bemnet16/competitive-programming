# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        minDepth = 0
        level = [root]
        
        while level:
            
            next_level = []
            minDepth += 1
            
            for node in level:
                
                if not (node.left or node.right):
                    return minDepth
                
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
            
            level = next_level