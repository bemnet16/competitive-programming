class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        answer = [-1, -1]
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                left = mid
                right = mid
                answer = [mid, mid]
            
            elif nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        if nums and nums[left] == target:
            
            l = 0
            r = left
            
            while l < r:
                
                m = l + (r - l) // 2
                if nums[m] == target:
                    r = m
                else:
                    l = m + 1
            
            answer[0] = l
            
            
            l = left
            r = len(nums) - 1
            
            while l < r:
                
                m = l + (r - l) // 2 + 1
                if nums[m] == target:
                    l = m 
                else:
                    r = m - 1
            
            answer[1] = l
            
        
        
        return answer
            
            
            
            
        