# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        pre_node = None
        isValid = True
        
        
        def dfs(root):
            
            nonlocal pre_node
            nonlocal isValid
            
            if root:
                
                dfs(root.left)
                
                if pre_node:
                    isValid = isValid and (pre_node.val < root.val)
                pre_node = root
                
                dfs(root.right)
        
        
        dfs(root)
        return isValid
            
