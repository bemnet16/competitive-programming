class Solution:
    def rob(self, nums: List[int]) -> int:
        
        money = [None] * len(nums)
        
        def dp(i):
        
            if i >= len(nums):
                return 0
            
            max_money = 0
            
            for j in range(i + 2, len(nums)):
                
                if  money[j]:
                    max_money = max(max_money, money[j])
                    
                else:
                    dp_j = dp(j)
                    money[j] = dp_j
                    max_money = max(max_money, dp_j)
            
            return nums[i] + max_money
        
        
        
        ans = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                ans = max(ans, dp(i))
        
        
        return ans