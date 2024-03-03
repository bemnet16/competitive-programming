class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False
        
        left_min = float("inf")
        right_max = float("inf")
        
        for num in nums:
            
            if num <= left_min:
                left_min = num
            
            elif num <= right_max:
                right_max = num
            
            else:
                return True
        
        
        return False