class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        subarray_sum = []
        
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                subarray_sum.append(cur_sum)
                
                
        subarray_sum.sort()
        
        ans = 0
        MOD = 10 ** 9 + 7
        for i in range(left - 1, right):
            ans = (ans + subarray_sum[i]) % MOD
        
        
        return ans