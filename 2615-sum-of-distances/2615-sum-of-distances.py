from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        # store prefix sum indexs of each num by there value 
        nums_prefix = defaultdict(list)
        
        # pointers for the stored prefix sum of each num
        pointers = defaultdict(int)
        
        # calculate the prefix sum of num and store in the nums_prefix
        for i,num in enumerate(nums):
            
            num_prefix = nums_prefix[num]
            
            if num_prefix:
                nums_prefix[num].append(num_prefix[-1] + i)
                
            else:
                nums_prefix[num].append(i)
                
        
        for i,num in enumerate(nums):
            
            pointer = pointers[num]
            num_prefix = nums_prefix[num]
            
            # reverese subtraction for the left of this index
            left = (pointer * i) - (num_prefix[pointer] - i)
            
            # regular subtraction for the right of this index
            right = (num_prefix[-1] - num_prefix[pointer]) - ((len(num_prefix) - pointer - 1) * i)
            
            # update nums inplace
            nums[i] = left + right
            
            # increse pointer for num by one
            pointers[num] += 1
        
        return nums