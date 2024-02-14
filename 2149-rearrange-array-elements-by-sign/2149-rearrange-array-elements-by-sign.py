class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        positives = []
        negatives = []
        
        for num in nums:
            
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
              
        positive_index = 0
        negative_index = 0
        
        for i in range(len(nums)):
            
            if i % 2 == 0:
                nums[i] = positives[positive_index]
                positive_index += 1
            
            else:
                nums[i] = negatives[negative_index]
                negative_index += 1
        
        return nums