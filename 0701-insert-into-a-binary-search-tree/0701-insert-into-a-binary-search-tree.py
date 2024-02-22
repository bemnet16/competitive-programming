# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
#         if not root:
#             return TreeNode(val)
        
#         if val < root.val:
#             root.left = self.insertIntoBST(root.left, val)
#         else:
#             root.right = self.insertIntoBST(root.right, val)
        
#         return root


        
        new_node = TreeNode(val)
        
        if not root:
            return new_node 
        
        cur = root
        stk = []
        
        while stk or cur:
            
            if cur:
                stk.append(cur)
                
                if cur.val > val:
                    cur = cur.left

                else:
                    stk.append(cur)
                    cur = cur.right
                
            else:
                cur = stk.pop()
                
                if not cur.left and val < cur.val:
                    cur.left = new_node
                else:
                    cur.right = new_node
                
                return root
        
        