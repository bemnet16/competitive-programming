class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        answer = 0
        cur_val = nums[0]

        for i in range(1, len(nums)):
            
            if cur_val >= nums[i]:
                
                diff = cur_val - nums[i]
                cur_val = nums[i] + (diff + 1)
                answer += (diff + 1)
                
            else:
                cur_val = nums[i]
        
        
        return answer