# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        stk = []
        stk.append((root, 1))
        answer = 0
        
        while stk:
            
            node, depth = stk.pop()
            
            if node:
                answer = max(answer, depth)
                
                if node.left:
                    stk.append((node.left, depth + 1))
                
                if node.right:
                    stk.append((node.right, depth + 1))
        
        return answer
        
