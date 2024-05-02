class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        
        seen = set()
        ans = -1
        
        for num in nums:
            if -num in seen:
                ans = max(ans, abs(num))
            seen.add(num)
        
        
        return ans