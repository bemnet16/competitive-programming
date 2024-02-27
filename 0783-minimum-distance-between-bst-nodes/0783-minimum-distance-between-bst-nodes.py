# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        self.min_diff = float("inf")
        self.pre_node = None
        
        def dfs(root):
            
            if root:
                dfs(root.left)
                
                if self.pre_node:
                    self.min_diff = min(self.min_diff, root.val - self.pre_node.val)
                self.pre_node = root
                
                dfs(root.right)
        
        
        dfs(root)
        return self.min_diff
        