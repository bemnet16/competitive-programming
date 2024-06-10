# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraverse(self, root):
            if root:
                self.inorderTraverse(root.left)
                self.all_nodes.append(root.val)
                self.inorderTraverse(root.right)
        

        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        self.all_nodes = []
        self.inorderTraverse(root)
        
        
        def balance(left, right):
            
            if left > right:
                return None
            
            mid = left + (right - left) // 2
            
            root = TreeNode(self.all_nodes[mid])
            root.left = balance(left, mid - 1)
            root.right = balance(mid + 1, right)
            
            return root
        
        
        
        return balance(0, len(self.all_nodes) - 1)