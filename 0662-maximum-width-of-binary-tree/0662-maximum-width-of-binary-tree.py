from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        queue = deque([(root, 1, 0)])
        preLevel, preVal = 0, 1
        answer = 1
        
        
        while queue:
            
            node, value, level = queue.popleft()
            
            if level > preLevel:
                preLevel = level
                preVal = value
            
            answer = max(answer, (value - preVal + 1))
            
            if node.left:
                queue.append((node.left, (value * 2), (level + 1)))
                
            if node.right:
                queue.append((node.right, (value * 2 + 1), (level + 1)))
        
        
        return answer
            
            
            
