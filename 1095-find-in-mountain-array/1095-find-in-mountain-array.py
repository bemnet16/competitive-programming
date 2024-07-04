# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        lg = mountain_arr.length()
        left, right = 1, lg - 2
        
        # find the peak value
        while left <= right:
            
            mid = left + (right - left) // 2
            leftVal, midVal, rightVal = mountain_arr.get(mid - 1), mountain_arr.get(mid), mountain_arr.get(mid + 1)
            if leftVal < midVal < rightVal:
                left = mid + 1
            elif leftVal > midVal > rightVal:
                right = mid - 1
            else:
                break

        # first search from left part
        low, high = 0, mid
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
        low, high = mid, lg - 1
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
            