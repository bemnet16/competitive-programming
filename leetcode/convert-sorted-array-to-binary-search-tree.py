# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def divide_conquer(arr, left, right):
            
            if left > right:
                return None
            
            mid = left + (right - left) // 2
            node = TreeNode(arr[mid])
            
            node.left = divide_conquer(arr, left, mid - 1)
            node.right = divide_conquer(arr, mid + 1, right)
            
            return node
        
        return divide_conquer(nums, 0, len(nums) - 1)
            
            
        
        