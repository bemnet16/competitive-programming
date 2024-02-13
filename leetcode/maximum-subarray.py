class Solution(object):
    def maxSubArray(self, nums):

        answer = float("-inf")
        prefix_sum = 0

        for i in range(len(nums)):

            prefix_sum += nums[i]
            answer = max(prefix_sum, answer)

            if prefix_sum < 0:
                prefix_sum = 0
        
        return answer
