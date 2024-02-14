class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        answer = 0
        current_value = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            
            if nums[i] > current_value:
                space = ceil(nums[i] / current_value)
                answer += (space - 1)
                current_value = nums[i] // space
                
            else:
                current_value = nums[i]
        
        return answer