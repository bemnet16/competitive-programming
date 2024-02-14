class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        
        def canFormTriangle(side1,side2,side3):
            
            if (side1 + side2) > side3 and (side2 + side3) > side1 and (side1 + side3) > side2:
                return True
            return False
        
        nums.sort(reverse = True)
        for i in range(len(nums) - 2):
            
            if canFormTriangle(nums[i], nums[i + 1], nums[i + 2]):
                return nums[i] + nums[i + 1] + nums[i + 2]
        
        return 0
                
        