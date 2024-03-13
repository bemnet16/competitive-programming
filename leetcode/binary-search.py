class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        def binarySearch(left, right):
            
            if left > right:
                return -1
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                return binarySearch(mid + 1, right)
            
            return binarySearch(left, mid - 1)
        
        
        
        
        return binarySearch(0, len(nums) - 1)