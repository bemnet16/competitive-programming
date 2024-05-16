class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return nums[0]
        
        cache = {}
        
        
        def dp(i, n):
            
            if i >= n:
                return 0
            
            max_money = 0
            for j in range(i + 2, len(nums)):
                
                if j in cache:
                    max_money = max(max_money, cache[j])
                
                else:
                    dp_house = dp(j, n)
                    max_money = max(max_money, dp_house)
                    
            cache[i] = max_money + nums[i]
            return cache[i]
        
        
        ans = 0
        ans = max(ans, dp(0, len(nums) - 1))
        cache = {}
        
        for i in range(1, len(nums)):
            ans = max(ans, dp(i, len(nums)))
            
        return ans
                
            