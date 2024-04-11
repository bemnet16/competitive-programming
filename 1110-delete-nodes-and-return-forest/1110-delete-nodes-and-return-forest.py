# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    
        if not root:
            return
    
        roots = [root]
        
        
        def dfs(root, node):
            
            if not root:
                return
            
            if root.val == node:
                if root.left:
                    roots.append(root.left)
                    root.left = None
                if root.right:
                    roots.append(root.right)
                    root.right = None
                roots.remove(root)
                return True
            
            if root.left:
                if root.left.val == node:
                    if root.left.left:
                        roots.append(root.left.left)
                    if root.left.right:
                        roots.append(root.left.right)
                    root.left = None
                    return True
            
            if root.right:
                if root.right.val == node:
                    if root.right.left:
                        roots.append(root.right.left)
                    if root.right.right:
                        roots.append(root.right.right)
                    root.right = None
                    return True
            
            if dfs(root.left, node):
                return True
            if dfs(root.right, node):
                return True
            
            return False
                    
                
        
        
        for node in to_delete:
            for root in roots:
                if dfs(root, node):
                    break
        
        return roots
                    
                    
                    