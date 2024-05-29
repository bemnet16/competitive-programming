# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        ans = []
        
        def dfs(root):
            
            if root:
                ans.append(root.val)
                
                left = dfs(root.left)
                right = dfs(root.right)
                
                if not left and not right:
                    return "(" + str(root.val) + ")"
                
                elif not left and right:
                    return "(" + str(root.val) + "()" + right + ")"
                
                elif left and not right:
                    return "(" + str(root.val) + left + ")"
                
                else:
                    return "(" + str(root.val) + left + right + ")"
                    
        
        
        r = dfs(root)
        return r[1:len(r) - 1]
        