class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        zeros = 1
        ans = 0
        
        for num in nums:
            if num == 0:
                ans += zeros
                zeros += 1
            else:
                zeros = 1
        
        return ans