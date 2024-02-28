# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        self.leftmost_val = None
        self.mx_row = float("-inf")
        
        def dfs(root, row):
            
            if root:
                dfs(root.left, row + 1)
                
                if self.mx_row < row:
                    self.mx_row = row
                    self.leftmost_val = root.val
                
                dfs(root.right, row + 1)
                
        
        dfs(root, 1)
        return self.leftmost_val
                
        