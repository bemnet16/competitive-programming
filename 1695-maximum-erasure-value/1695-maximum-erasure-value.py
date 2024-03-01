class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        seen = set()
        left = 0
        score = 0
        max_score = 0
        
        for i in range(len(nums)):
            
            score += nums[i]
            
            while nums[i] in seen:
                
                seen.remove(nums[left])
                score -= nums[left]
                
                left += 1
            
            seen.add(nums[i])
            max_score = max(max_score, score)
        
        
        return max_score
            
            
        