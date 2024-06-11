class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        
        num_set = set(nums)
        
        for num in nums:
            reverse = int(str(num)[::-1])
            num_set.add(reverse)

            
        return len(num_set)