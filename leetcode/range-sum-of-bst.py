# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.total = 0
        
    def inorderSearch(self, root, low, high):
        
        if root:
            self.inorderSearch(root.left, low, high)
            
            if low <= root.val and root.val <= high:
                self.total += root.val
            
            self.inorderSearch(root.right, low, high)
        
        return root
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.inorderSearch(root, low, high)
        
        return self.total
        