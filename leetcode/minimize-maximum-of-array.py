class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        answer = nums[0]
        total = nums[0]
        
        for i in range(1, len(nums)):
            total += nums[i]
            answer = max(answer, ceil(total / (i + 1)))
        
        
        return answer