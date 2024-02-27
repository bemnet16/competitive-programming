# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        self.mod_dict = defaultdict(int)
        self.mx = float("-inf")
        
        def inorder(root):
            if root:
                inorder(root.left)
                self.mod_dict[root.val] += 1
                self.mx = max(self.mx, self.mod_dict[root.val])   
                inorder(root.right)
            
        inorder(root)
        
        answer = [key for key in self.mod_dict if self.mod_dict[key] == self.mx]
        
        return answer
        
        