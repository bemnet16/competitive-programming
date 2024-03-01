class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        answer = [-1] * n
        
        stk = []
        
        for i in range(2 * n):
            
            while stk and nums[stk[-1]] < nums[i % n]:
                answer[stk.pop()] = nums[i % n]
            
            
            stk.append(i % n)
            
        
        return answer
        