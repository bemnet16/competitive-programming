# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.values = []
        
    def inorderSearch(self,root):
        
        if root:
            self.inorderSearch(root.left)
            self.values.append(root.val)
            self.inorderSearch(root.right)
        
        return self.values
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.inorderSearch(root)
        
        temp = self.values.copy()
        s = set(temp)
        
        if len(s) != len(self.values):
            return False
        
        temp.sort()
        
        return temp == self.values
        