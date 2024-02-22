# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        queue = [[root]]
        answer = []
        idx = 0
        
        while queue:
            
            current_stack = []
            anT = []
            current = queue.pop(0)
            
            for node in current:
                anT.append(node.val)
                
                if node.left:
                    current_stack.append(node.left)
                if node.right:
                    current_stack.append(node.right)
                    
            if anT:
                if idx % 2 == 1:
                    answer.append(anT[::-1])
                else:
                    answer.append(anT)
                    
            if current_stack:
                queue.append(current_stack)
            
            idx += 1
        
        return answer
                    
                    
            
                
        