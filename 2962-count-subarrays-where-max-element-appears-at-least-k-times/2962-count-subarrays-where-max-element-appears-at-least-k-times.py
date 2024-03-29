from collections import deque

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        max_num = max(nums)
        indexes = deque()
        answer = 0
        
        for i, num in enumerate(nums):
            
            if num == max_num:
                if len(indexes) == k:
                    indexes.popleft()
                indexes.append(i)
            
            
            if len(indexes) == k:
                answer += (indexes[0] + 1)
        
        
        return answer
        