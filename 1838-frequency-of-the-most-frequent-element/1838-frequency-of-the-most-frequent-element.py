class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        ans = 1
        l = 0
        
        for r in range(1, len(nums)):
            
            if nums[r] > nums[r - 1]:
                
                diff = nums[r] - nums[r - 1]
                
                while l <= r and k < ((r - l) * diff):
                        k += nums[r - 1] - nums[l]
                        l += 1
                
                k -= ((r - l) * diff)
                
            ans = max(ans, r - l + 1)
        
        return ans
        