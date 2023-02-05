class Solution(object):
    def targetIndices(self, nums, target):
       
       #Sort the given list in increasing order
       for i in range(len(nums)):
           for j in range((i + 1), len(nums)):
               if nums[i] > nums[j]:
                   nums[i],nums[j] = nums[j],nums[i]
                    
       indices = []
       for k in range(len(nums)):
           if target == nums[k]:
                indices.append(k)
       return indices
