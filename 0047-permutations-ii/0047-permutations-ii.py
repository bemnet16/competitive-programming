class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        seen = [0] * len(nums)
        answer = set()
        
        def backtrack(perm):
            
            if len(perm) == len(nums):
                answer.add(tuple(perm.copy()))
                return
            
            
            for i in range(len(nums)):
                
                if seen[i] == 1:
                    continue
                
                seen[i] = 1
                perm.append(nums[i])
                backtrack(perm)
                
                seen[i] = 0
                perm.pop()
        
        
        backtrack([])
        return answer
        