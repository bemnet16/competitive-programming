# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def f(lis):
            
            if not lis:
                return None
            
            if len(lis) == 1:
                return TreeNode(lis[0])
            
            mid = len(lis) // 2
            new_node = TreeNode(lis[mid])
            
            new_node.left = f(lis[:mid])
            new_node.right = f(lis[mid + 1:])
            
            return new_node
        
        return f(nums)
            
            
        
        