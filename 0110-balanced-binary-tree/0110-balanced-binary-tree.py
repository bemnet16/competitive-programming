# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            
            if not root:
                return 1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            
            
            if abs(left - right) > 1 or not left or not right:
                return False
            
            return 1 + max(left, right)
        
        
        return bool(dfs(root))
            
        