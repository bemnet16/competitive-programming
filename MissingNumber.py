class Solution(object):
    def missingNumber(self, nums):
        lg=len(nums)+1
        temp = set(nums)
        for i in range(lg):
            if i not in temp:
                return i
        
