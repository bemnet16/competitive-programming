class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Length of nums is (n + 1)
#         n = len(nums) - 1
        
#         expected_sum = (n * (n + 1)) // 2
#         actual_sum = sum(nums)
        
#         # The difference between actual_sum and expected_sum is the duplicated Number
#         return actual_sum - expected_sum
        
    
        num_set = set()
        for num in nums:
            if num in num_set:
                return num
            num_set.add(num)
        