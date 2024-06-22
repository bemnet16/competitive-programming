class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        cache = defaultdict(int)
        
        def dp(cur, i):
            
            if i in cache:
                return cache[i]
            
            mx_sub = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > cur:
                     mx_sub = max(mx_sub, dp(nums[j], j))
                    
            
            cache[i] = 1 + mx_sub
            return cache[i]
        
        
        ans = 0
        for i, num in enumerate(nums):
            ans = max(ans, dp(num, i))
        
        return ans