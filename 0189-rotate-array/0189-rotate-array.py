class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        if k % len(nums) == 0:
            return nums
        
        
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        

        left, right = 0, (k % len(nums)) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        
        left, right = (k % len(nums)), len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
            