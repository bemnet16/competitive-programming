class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        nums = list(map(str, digits))
        nums = "".join(nums)
        nums = int(nums) + 1
        nums = str(nums)
        
        answer = [int(n) for n in nums]
        return answer
        