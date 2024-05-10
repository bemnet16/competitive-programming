class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        memo = defaultdict(int)
        
        def dp(idx, cur_sum):
            
            
            if idx == len(nums):
                if cur_sum == target:
                    return 1
                return 0
            
            if (idx, cur_sum) in memo:
                return memo[(idx, cur_sum)]
            
            ptve = dp(idx + 1, cur_sum + nums[idx])
            ntve = dp(idx + 1, cur_sum - nums[idx])
            
            memo[(idx, cur_sum)] = ptve + ntve
            
            return memo[(idx, cur_sum)]
        
        
        
        
        return dp(0, 0)