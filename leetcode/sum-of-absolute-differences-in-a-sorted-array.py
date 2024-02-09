class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            su = prefix[i - 1] + nums[i]
            prefix.append(su)
        
        for i in range(len(nums)):
            l_result = (i * nums[i]) - (prefix[i] - nums[i])
            r_result = (prefix[-1] - prefix[i]) - ((len(nums) - i - 1) * nums[i])
            nums[i] = l_result + r_result
        
        return nums