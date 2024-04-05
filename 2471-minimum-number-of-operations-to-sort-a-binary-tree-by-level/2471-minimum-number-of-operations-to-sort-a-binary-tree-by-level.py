# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        def sortingArr(arr):
            
            n = len(arr)
            ans = 0
            temp = arr.copy()
            h = {}
            temp.sort()

            for i in range(n):
                h[arr[i]] = i
            init = 0

            for i in range(n):
                if (arr[i] != temp[i]):
                    ans += 1
                    init = arr[i]
                    arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]
                    h[init] = h[temp[i]]
                    h[temp[i]] = i

            return ans
                           
                
                    
        level = [root]
        operations = 0
        
        while level:
            
            next_level = []
            level_elements = []
            
            for node in level:
                
                level_elements.append(node.val)
                
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
            

            operations += sortingArr(level_elements)
            level = next_level
        
        
        return operations
                
                
            
        