# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.vals = None
        self.count = 0
        
    def inorderSearch(self, root, k):
        if root:
            self.inorderSearch(root.left, k)
            self.count += 1
            if self.count == k:
                self.vals = root.val
                return
            self.inorderSearch(root.right, k)
        return root
    
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.inorderSearch(root, k)
        return self.vals
        