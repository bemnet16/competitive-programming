class Solution(object):
    def findDuplicates(self, nums):
        
        answer = set()
        
        for i in range(len(nums)):
            
            while i != (nums[i] - 1):
                
                temp = nums[i] - 1
                if nums[i] == nums[temp]:
                    answer.add(nums[i])
                    break
                
                else:
                    nums[i], nums[temp] = nums[temp], nums[i]
        
        
        return answer
            