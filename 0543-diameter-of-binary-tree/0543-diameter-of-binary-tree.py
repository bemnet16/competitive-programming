# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_diameter = float("-inf")
        
        
        def diameterOfRoot(root):
            
            if not root:
                return 0
            
            left_height = diameterOfRoot(root.left)
            right_height = diameterOfRoot(root.right)
            
            self.max_diameter = max(self.max_diameter, (left_height + right_height))
            
            return 1 + max(left_height, right_height)
        
        
        
        diameterOfRoot(root)
        return self.max_diameter