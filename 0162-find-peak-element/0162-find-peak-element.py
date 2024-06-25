class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            if mid > 0 and nums[mid - 1] > nums[mid]:
                high = mid - 1
            elif mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
                low = mid + 1
            else:
                return mid
