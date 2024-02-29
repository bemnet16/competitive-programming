class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        t_sum = 0
        
        for i in range(k):
            t_sum += nums[i]
        
        average = t_sum / k
        max_average = average
        
        for i in range(k, len(nums)):
            
            t_sum -= nums[i - k]
            t_sum += nums[i]
            
            average = t_sum / k

            max_average = max(max_average, average)
        
        
        return max_average