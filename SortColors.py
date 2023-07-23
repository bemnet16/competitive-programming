class Solution(object):
    def sortColors(self, nums):
        
        red,whi,blu=[],[],[]
        for num in nums:
            if num==0: red.append(num)
            elif num==1: whi.append(num)
            else: blu.append(num)
        nums[:] = red+whi+blu
        return nums

        # for i in range(len(nums)):
        #     for j in range((i + 1),len(nums)):
        #         if nums[i] > nums[j]:
        #             nums[i],nums[j] = nums[j],nums[i]

        #It is also possible algorithm for the given problem
        
        # counter_nums = [0] * 3   #Since there are only 3(red,white,blue) values
        # for i in nums:
        #     counter_nums[i] += 1

        # new_nums = []
        # for i in range(3):
        #     for j in range(counter_nums[i]):
        #         new_nums.append(i)

        

        
