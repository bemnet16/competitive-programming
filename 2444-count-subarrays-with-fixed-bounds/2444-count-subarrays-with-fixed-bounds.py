class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        mini, maxi, badi = -1, -1, -1
        answer = 0
        
        for i, num in enumerate(nums):
            
            if (num < minK) or (num > maxK):
                badi = i
            
            if num == minK:
                mini = i
            
            if num == maxK:
                maxi = i
            
            answer += max(0, min(mini, maxi) - badi)
        
        
        return answer
        
        