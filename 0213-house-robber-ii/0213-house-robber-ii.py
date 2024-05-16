class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return nums[0]
        
        cache = {}
        
        
        def dp(i, isFirst):
            
            if (i >= len(nums)) or (i + 1 == len(nums) and isFirst):
                return 0
            
            max_money = 0
            for j in range(i + 2, len(nums)):
                
                if (j, isFirst) in cache:
                    max_money = max(max_money, cache[(j, isFirst)])
                
                else:
                    dp_house = dp(j, isFirst)
                    max_money = max(max_money, dp_house)
                    
            cache[(i, isFirst)] = max_money + nums[i]
            return cache[(i, isFirst)]
        
        
        ans = 0
        ans = max(ans, dp(0, True))
        for i in range(1, len(nums)):
            ans = max(ans, dp(i, False))
            
        return ans
                
            