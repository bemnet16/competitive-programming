class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        track = {}
        
        for i, num in enumerate(nums):
            
            if (target - num) in track:
                return [track[target - num], i]
            
            track[num] = i
        
