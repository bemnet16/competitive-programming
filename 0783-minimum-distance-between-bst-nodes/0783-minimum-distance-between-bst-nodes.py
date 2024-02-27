# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        self.min_diff = float("inf")
        self.pre_node = -100000000000
        
        def dfs(root):
            
            if root:
                dfs(root.left)
                
                self.min_diff = min(self.min_diff, root.val - self.pre_node)
                self.pre_node = root.val
                
                dfs(root.right)
        
        
        dfs(root)
        return self.min_diff
        