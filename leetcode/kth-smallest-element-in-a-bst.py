# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.vals = []
        
    def inorderSearch(self, root):
        if root:
            self.inorderSearch(root.left)
            self.vals.append(root.val)
            self.inorderSearch(root.right)
        return root
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.inorderSearch(root)
        return self.vals[k - 1]
        