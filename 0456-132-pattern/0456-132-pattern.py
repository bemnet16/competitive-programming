class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        tillMin = nums[0]
        
        for i, num in enumerate(nums):
            
            while stack and num >= stack[-1][0]:
                stack.pop()
            
            if stack and num > stack[-1][1]:
                return True
            
            stack.append((num, tillMin))
            tillMin = min(tillMin, num)
        
        
        return False