class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stk = []
        mi = nums[0]
        
        for i, num in enumerate(nums[1:]):
            
            while stk and num >= stk[-1][0]:
                stk.pop()
            
            if stk and num > stk[-1][1]:
                    return True
                
            stk.append([num, mi])
            mi = min(mi, num)
        
        
        
        return False
                
                