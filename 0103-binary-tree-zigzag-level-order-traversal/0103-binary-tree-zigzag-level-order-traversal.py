# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        stk = [[root]]
        ans = []
        idx = 0
        
        while stk:
            
            stT = []
            anT = []
            temp = stk.pop(0)
            
            for n in temp:
                anT.append(n.val)
                
                if n.left:
                    stT.append(n.left)
                if n.right:
                    stT.append(n.right)
                    
            if anT:
                if idx % 2 == 1:
                    ans.append(anT[::-1])
                else:
                    ans.append(anT)
            if stT:
                stk.append(stT)
            
            idx += 1
        
        return ans
                    
                    
            
                
        