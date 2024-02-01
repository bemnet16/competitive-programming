class Solution(object):
    def searchRange(self, nums, target):
        start = -1
        left,right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                start = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        
        end = -1
        left,right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                end = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        
        return [start,end]
        