class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        answer_count = 0
        prefix_sum = 0
        nums_pointer = 0
        
        while True:
            
            next_sum = prefix_sum + 1
            
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
        