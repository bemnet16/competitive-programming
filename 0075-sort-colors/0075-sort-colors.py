class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        colors = [0, 0, 0]
        for num in nums:
            colors[num] += 1
        
        
        idx = 0
        for c in range(3):
            for i in range(colors[c]):
                nums[idx] = c
                idx += 1