class Solution(object):
    def findDisappearedNumbers(self, nums):
        
        answer = set()
        
        for i in range(len(nums)):
            
            while i != (nums[i] - 1):
                
                temp = nums[i] - 1
                if nums[i] == nums[temp]:
                    break
                
                else:
                    nums[i], nums[temp] = nums[temp], nums[i]
        
        
        for i, num in enumerate(nums):
            
            if i != (num - 1):
                answer.add(i + 1)
            
            
            
            
            
        return answer