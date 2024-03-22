class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        for i in range(len(nums)):
            
            while i != (nums[i] - 1):
                
                temp = nums[i] - 1
                if nums[i] == nums[temp]:
                    return nums[i]
                
                else:
                    nums[i], nums[temp] = nums[temp], nums[i]
        
        
        
        # Length of nums is (n + 1)
#         n = len(nums) - 1
        
#         expected_sum = (n * (n + 1)) // 2
#         actual_sum = sum(nums)
        
#         # The difference between actual_sum and expected_sum is the duplicated Number
#         return actual_sum - expected_sum
        
    
#         num_set = set()
#         for num in nums:
#             if num in num_set:
#                 return num
#             num_set.add(num)
        