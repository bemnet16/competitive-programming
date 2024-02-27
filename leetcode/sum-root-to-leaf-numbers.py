# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.total = 0
        self.temp = 0
        
    def preorder(self, root):
        
        if root:
            self.temp = (self.temp * 10 + root.val)
            
            if not root.left and not root.right:
                self.total += self.temp
                self.temp //= 10
                return
            
            self.preorder(root.left)
            self.preorder(root.right)
            
            self.temp //= 10
        
        return root
                
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.preorder(root)
        
        return self.total
        
        
        