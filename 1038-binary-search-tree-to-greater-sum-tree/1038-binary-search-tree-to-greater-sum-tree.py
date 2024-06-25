# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def dfs(root):
            
            nonlocal cur
            
            if root:
                dfs(root.right)
                root.val += cur
                cur = root.val
                dfs(root.left)
            
            
        cur = 0
        dfs(root)
        return root