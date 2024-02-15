class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        answer_count = 0   # count the number or patched elements
        
        # the prefix sum of the numbers. 
        #it is also tell us until this number we can get a subset of numbers whose sum is equal to the intended number
        prefix_sum = 0
        nums_pointer = 0   # index value for the procided nums element
        
        # iterate till we get prefix sum greater than 'n' 
        #/ this mean until 'n' we can get a number whose value is sum of subset of previous numbers 
        while True:
            
            next_sum = prefix_sum + 1
            
            # the pointer is out of range so we need to patch each element whose sum can't be found by summation of number from the previous
            if nums_pointer == len(nums):
                answer_count += 1
                prefix_sum += next_sum
            
            
            elif next_sum < nums[nums_pointer]:
                answer_count += 1
                prefix_sum += next_sum
            
            else:
                prefix_sum += nums[nums_pointer]
                nums_pointer += 1
            
            if prefix_sum >= n:
                return answer_count
        