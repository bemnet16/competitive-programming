# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        answer = 0
        
        def dfs(node, stk):
            
            nonlocal answer
            
            if len(stk) == 3 and not stk[0] % 2:
                answer += node.val
                
            if node.left:
                tmp = stk.copy()
                if len(tmp) == 3:
                    dfs(node.left, tmp[1:] + [node.left.val])
                else:
                    dfs(node.left, tmp + [node.left.val])
            
            if node.right:
                tmp = stk.copy()
                if len(tmp) == 3:
                    dfs(node.right, tmp[1:] + [node.right.val])
                else:
                    dfs(node.right, tmp + [node.right.val])
            
            
        
        dfs(root, [root.val])
        return answer
    
    
    