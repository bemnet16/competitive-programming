class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
       
       new_nums = []
       for i in range(len(nums)):
           count = 0
           for j in range(len(nums)):
               if nums[i] > nums[j]:
                   count += 1
           new_nums.append(count)

       return new_nums
