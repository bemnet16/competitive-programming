class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res, acc = 0, 0
        trk = defaultdict(int)
        
        for i in range(len(nums)):
            acc += nums[i]
            if acc == goal:
                res += 1
            if acc - goal in trk:
                res += trk[acc - goal]
            trk[acc] += 1
        
        return res