class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        
        while low < high:
            
            mid = low + (high - low) // 2
            
            if nums[mid - 1] == nums[mid]:
                if (mid - low + 1) % 2 == 1:
                    high = mid - 2
                else:
                    low = mid + 1
                
            else:
                if (mid - low) % 2 == 1:
                    high = mid - 1
                else:
                    low = mid
        
        return nums[low]
        