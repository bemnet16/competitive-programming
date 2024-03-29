class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
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
                break
                
                
        
        if nums[low] == target:
            return low
        
        if len(nums) == 1:
            return -1
        
        
        
        if nums[0] <= target and low > 0 and target <= nums[low - 1]:
            high = low - 1
            low = 0
            
        else:
            low = low + 1
            high = len(nums) - 1
            
            
            
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            if target < nums[mid]:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
                    
        
        return high if nums[high] == target else -1
                
        