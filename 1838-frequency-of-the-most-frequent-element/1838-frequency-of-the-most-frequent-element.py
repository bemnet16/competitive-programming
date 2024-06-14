class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        ans = 1
        l = 0
        cur = nums[0]
        
        for r in range(1, len(nums)):
            
            if nums[r] > cur:
                
                lg = r - l
                diff = nums[r] - cur
                
                while l <= r and k < (lg * diff):
                        k += cur - nums[l]
                        l += 1
                        lg -= 1
                
                
                if k >= (lg * diff):
                    k -= (lg * diff)
                    cur = nums[r]
                
            ans = max(ans, r - l + 1)
        
        return ans
        