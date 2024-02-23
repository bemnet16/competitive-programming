# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.vals = []
        self.count = 0
        
    def inorderSearch(self, root):
        
        if root:
            self.inorderSearch(root.left)
            if root.val not in self.vals:
                self.vals.append(root.val)
               
            self.inorderSearch(root.right)
        
        return root
    
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        self.inorderSearch(root)
        
        if len(self.vals) <= 1:
            return -1
        
        self.vals.sort()
        
        return self.vals[1]