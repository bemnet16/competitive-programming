class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        MOD = 10 ** 9 + 7
        
        nums.sort()
        left, right = 0, len(nums) - 1
        subsequences = 0
        
        while left <= right:
            
            cur_sum = nums[left] + nums[right]
            
            if cur_sum > target:
                right -= 1
            
            else:
                subsequences = (subsequences + (2 ** (right - left))) % MOD
                left += 1
        
        
        return subsequences %  MOD
        