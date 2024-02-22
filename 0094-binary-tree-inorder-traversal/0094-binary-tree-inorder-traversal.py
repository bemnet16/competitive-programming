# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []
        
        stk = []
        cur = root
        answer = []
        
        while cur or stk:
            
            if cur:
                stk.append(cur)
                cur = cur.left
            
            else:
                cur = stk.pop()
                answer.append(cur.val)
                cur = cur.right
        
    
        return answer