# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        left, right = 1, mountain_arr.length() - 2
        
        # find the peak value
        while left < right:
            
            mid = left + (right - left) // 2
            
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

                
        
        # first search from left part
        low, high = 0, left
        while low <= high:
            
            mid = low + (high - low) // 2
            val = mountain_arr.get(mid)
            
            if val == target:
                return mid
            
            elif val < target:
                low = mid + 1
            
            else:
                high = mid - 1
            
        
        
        # finally search on the right part
        low, high = left, mountain_arr.length() - 1
        while low <= high:
            
            mid = low + (high - low) // 2
            val = mountain_arr.get(mid)
            
            if val == target:
                return mid
            
            elif val < target:
                high = mid - 1
            
            else:
                low = mid + 1
        
        
        return -1
            