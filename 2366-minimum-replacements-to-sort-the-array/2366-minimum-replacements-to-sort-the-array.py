class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        answer = 0
        temp = nums[-1]
        
        for i in range(len(nums) - 1, -1, -1):
            space = ceil(nums[i] / temp)
            answer += (space - 1)
            temp = nums[i] // space
        
        return answer
            
        
       