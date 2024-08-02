class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        ones = sum(nums)
        
        if ones == 0: 
            return 0
        
        nums.extend(nums[:ones])
        cur = 0
        ans = float("inf")
        
        for i in range(ones - 1):
            cur += nums[i]
        
        l = 0
        for i in range(ones - 1, len(nums)):
            cur += nums[i]
            ans = min(ans, ones - cur)
            cur -= nums[l]
            l += 1
        
        
        return ans
        
        
        