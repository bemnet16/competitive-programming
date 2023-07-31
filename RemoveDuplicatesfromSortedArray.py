class Solution(object):
    def removeDuplicates(self, nums):
        # for i in nums:
        #     for j in range(1,nums.count(i)):
        #         nums.remove(i)
        # return len(nums)

        i=0
        for j in range(len(nums)):
            if i+1 < len(nums) and nums[i]==nums[i+1]: nums.remove(nums[i])
            else: i+=1
        return i
