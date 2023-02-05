class Solution(object):
    def sortColors(self, nums):

      #It can be solved easily by using insertion sort   
        for i in range(len(nums)):
            for j in range((i + 1),len(nums)):
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]

        #It is also possible algorithm for the given problem
        
        # counter_nums = [0] * 3   #Since there are only 3(red,white,blue) values
        # for i in nums:
        #     counter_nums[i] += 1

        # new_nums = []
        # for i in range(3):
        #     for j in range(counter_nums[i]):
        #         new_nums.append(i)
