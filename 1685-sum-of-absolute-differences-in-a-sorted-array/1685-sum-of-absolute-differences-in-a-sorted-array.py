class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        nums_total = sum(nums)
        temp_sums = 0
        result = []
        for i in range(len(nums)):
            left = abs((i * nums[i]) - temp_sums)
            right = abs(((len(nums) - i) * nums[i]) - (nums_total - temp_sums))
            result.append(left + right)
            temp_sums += nums[i]
        
        return result