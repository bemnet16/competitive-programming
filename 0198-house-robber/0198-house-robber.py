class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return nums[0]
        
        money = [-1] * len(nums)
        
        
        def dp(i):
        
            max_money = 0
            
            for house in range(i + 2, len(nums)):
                
                if  money[house] != -1:
                    max_money = max(max_money, money[house])
                    
                else:
                    dp_house = dp(house)
                    money[house] = dp_house
                    max_money = max(max_money, dp_house)
            
            return nums[i] + max_money
        
        
        
        return max(dp(0), dp(1))
