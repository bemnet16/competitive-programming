# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []
        
        stk = []
        answer = []
        stk.append(root)
        
        while stk:
            
            cur = stk.pop()
            answer.append(cur.val)
            
            if cur.right:
                stk.append(cur.right)
            
            if cur.left:
                stk.append(cur.left)
        
        return answer
        
        