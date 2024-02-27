from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        queue = deque()
        queue.append([root])
        answer = []
        level = 0
        
        while queue:
            
            current_stack = []
            sub_answer = []
            current = queue.popleft()
            
            for node in current:
                sub_answer.append(node.val)
                
                if node.left:
                    current_stack.append(node.left)
                if node.right:
                    current_stack.append(node.right)
                    
            if sub_answer:
                if level % 2 == 1:
                    answer.append(sub_answer[::-1])
                else:
                    answer.append(sub_answer)
                    
            if current_stack:
                queue.append(current_stack)
            
            level += 1
        
        
        return answer
                    
                    
            
                
        