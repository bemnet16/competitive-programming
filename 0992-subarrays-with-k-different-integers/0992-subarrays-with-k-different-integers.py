class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def numOfSubarray(k):
            frequency = defaultdict(int)
            totSubarray = 0
            left = 0
            
            for right, num in enumerate(nums):
                
                frequency[num] += 1
                
                while len(frequency) > k:
                    if frequency[nums[left]] == 1:
                        del frequency[nums[left]]
                    else:
                        frequency[nums[left]] -= 1
                    left += 1
                
                totSubarray += (right - left + 1)
            
            return totSubarray
        
        
        
        return numOfSubarray(k) - numOfSubarray(k - 1)
                
        
        