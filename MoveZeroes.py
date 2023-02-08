class Solution(object):
    def moveZeroes(self, nums):

        lf = -1
        for i in xrange(len(nums)):
            if nums[i] != 0:
                lf += 1
                nums[lf], nums[i] = nums[i], nums[lf]
