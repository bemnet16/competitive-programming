class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)

        # The differce is the missing number
        return expected_sum - actual_sum
        
        
        #### Cyclic sort approach ####
#         nums.append(len(nums))
    
#         for i in range(len(nums)):

#             while i != nums[i] and nums[i] != nums[nums[i]]:

#                 temp = nums[i]
#                 nums[i], nums[temp] = nums[temp], nums[i]

#         for i, num in enumerate(nums):

#             if i != nums[i]:
#                 return i

#         return len(nums) - 1

    
    



        
    