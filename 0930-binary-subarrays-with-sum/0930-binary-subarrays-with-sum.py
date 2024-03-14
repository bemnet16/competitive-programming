class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        
        di = defaultdict(int)
        di[0] = 1
        pre = 0
        ans = 0
        
        for i in range(len(nums)):
            
            pre += (nums[i] == 1)
            
            ans += di[pre - goal]
            
            di[pre] += 1
            
        
        
        return ans