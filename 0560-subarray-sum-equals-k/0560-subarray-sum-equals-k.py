class Solution(object):
    def subarraySum(self, nums, k):
        res, acc = 0, 0
        trk = defaultdict(int)
        
        for i in range(len(nums)):
            acc += nums[i]
            if acc == k:
                res += 1
            if acc - k in trk:
                res += trk[acc - k]
            trk[acc] += 1
        
        return res
        