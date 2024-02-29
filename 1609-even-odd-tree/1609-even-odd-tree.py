# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        stack = [[root]]
        level = 0
        
        while stack:
            
            temp_stack = []
            popped_nodes = stack.pop()
            pre_val = None
            
            for node in popped_nodes:
                
                if level & 1:
                    
                    if node.val & 1:
                        return False
                    
                    else:
                        
                        if pre_val:
                            
                            if pre_val <= node.val:
                                return False
                            
                            else:
                                pre_val = node.val
                                
                        else:
                            pre_val = node.val
                  
                
                else:
                    
                    if node.val & 1:
                        
                        if pre_val:
                            
                            if pre_val >= node.val:
                                return False
                            
                            else:
                                pre_val = node.val
                                
                                
                        else:
                            pre_val = node.val
                            
                    else:
                        return False
                    
                    
                
                if node.left:
                    temp_stack.append(node.left)
                
                if node.right:
                    temp_stack.append(node.right)
                    
            
            if temp_stack:
                stack.append(temp_stack)
                
            level += 1
            
            
            
        return True
        