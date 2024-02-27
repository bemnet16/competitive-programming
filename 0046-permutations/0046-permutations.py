class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        
        def backtrack(index, permut):
            
            if len(permut) == len(nums):
                answer.append(permut.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in permut:
                    continue
                permut.append(nums[i])
                backtrack(i + 1, permut)
                permut.pop()
            
        backtrack(0, [])
        return answer