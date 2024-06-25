class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums = sorted(set(nums))
        ans = n
        r = 0
        
        for l in range(len(nums)):
            
            while r < len(nums) and nums[r] < nums[l] + n:
                r += 1
            
            window = r - l
            ans = min(ans, n - window)
        
        
        return ans
        