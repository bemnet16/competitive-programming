class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        
        def backtrack(permut):
            
            if len(permut) == len(nums):
                answer.append(permut.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in permut:
                    continue
                permut.append(nums[i])
                backtrack(permut)
                permut.pop()
            
        backtrack([])
        return answer