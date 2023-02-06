class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = []
        for i in range(len(nums)//2):
            result.append(nums[len(nums)-i-1] + nums[i])
        return max(result)
