class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        answer, prefix = 0, 0
        track = defaultdict(int)
        track[0] = 1
        
        for i in range(len(nums)):
            prefix += nums[i]
            reminder = prefix % k
            
            if reminder in track:
                answer += track[reminder]
            track[reminder] += 1
        
        return answer
        
        