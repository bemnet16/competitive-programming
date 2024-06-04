class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()
        answer = 0
        
        for i in range(len(nums) - 1, -1, -1):
            
            v = nums.pop()
            
            a = bisect_left(nums, lower - v)
            b = bisect_right(nums, upper - v)
            
            answer += (b - a)
        
        
        return answer