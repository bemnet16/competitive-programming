class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        target = sum(nums) - x
        
        if target < 0:
            return -1
        
        max_subarray = -1
        _sum = 0
        
        l = 0
        for r in range(len(nums)):
            
            _sum += nums[r]
            
            while _sum > target:
                _sum -= nums[l]
                l += 1
            
            if _sum == target:
                max_subarray = max(max_subarray, (r - l + 1))
            
        
        
        return -1 if max_subarray == -1 else len(nums) - max_subarray