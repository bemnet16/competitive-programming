class Solution(object):
    def sortJumbled(self, mapping, nums):
        
        def mapped(num):
            
            temp = 0
            for i in num:
                temp = temp * 10 + mapping[int(i)]
            
            return temp
        
        
        for i, num in enumerate(nums):
            
            nums[i] = [num, mapped(str(num))]
        
        
        nums.sort(key=lambda x:x[1])
        
        nums = [num for num, mapped in nums]
        
        return nums
        