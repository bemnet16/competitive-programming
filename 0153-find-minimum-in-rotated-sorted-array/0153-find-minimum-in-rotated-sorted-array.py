class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            if nums[low] > nums[high]:
                if nums[mid] > nums[high]:
                    low = mid + 1
                
                else:
                    high = mid
            
            elif nums[low] < nums[high]:
                if nums[mid] < nums[high]:
                    high = mid - 1
                
                else:
                    low = mid
            
            else:
                return nums[low]
        
        return nums[low]
        