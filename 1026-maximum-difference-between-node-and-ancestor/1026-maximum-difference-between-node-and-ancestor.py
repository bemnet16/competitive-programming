# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(root):
            
            nonlocal ans
            
            if not root:
                return [float('-inf'), float('inf')]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            _max = max(root.val, left[0], right[0])
            _min = min(root.val, left[1], right[1])
            
            ans = max(ans, abs(root.val - _max), abs(root.val - _min))
            
            return [_max, _min]
        
        
        
        ans = float('-inf')
        dfs(root)
        return ans