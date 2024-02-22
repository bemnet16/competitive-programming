# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderSuccessor(self, root):
        
        current = root
        while current and current.left:
            current = current.left
        
        return current
    
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            
            if not root.left and not root.right:
                return None
            
            elif not root.left or not root.right:
                if root.left:
                    return root.left
                else:
                    return root.right
            
            else:
                
                successor = self.inorderSuccessor(root.right)
                
                root.val = successor.val
                
                root.right = self.deleteNode(root.right, successor.val)
                
        return root
        
        