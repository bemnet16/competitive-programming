class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()
        
        for i in range(101):
            if i == len(nums) - bisect_left(nums, i):
                return i
        
        return -1
        