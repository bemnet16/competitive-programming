class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        answer = 0
        
        for i in range(n):
            for j in range((i + 1), n):
                for k in range((j + 1), n):
                    for l in range((k + 1), n):
                        
                        a, b, c, d = nums[i], nums[j], nums[k], nums[l]
                        if (a + b + c) == d:
                            if (i < j) and (j < k) and (k < l):
                                answer += 1
        
        return answer