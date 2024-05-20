class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        answer = 0
        
        def backtrack(i, xor):
            
            nonlocal answer
            
            if i >= len(nums):
                answer += xor
                return 
            
            
            backtrack(i + 1, xor ^ nums[i])
            backtrack(i + 1, xor)
        
        
        
        backtrack(0, 0)
        return answer
                
        