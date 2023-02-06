class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        inter_change = True
        while inter_change == True:
            inter_change = False
            for i in range(1, len(nums)-1):
                if (nums[i-1] + nums[i+1]) / 2 == nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    inter_change = True
                    
        return nums
