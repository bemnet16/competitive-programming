class Solution(object):
    def minSubArrayLen(self, target, nums):
        ans=len(nums)+1
        i,j,t_sum=0,0,0
        while i<len(nums):
            t_sum+=nums[i]
            while t_sum>=target:
                if t_sum>=target:
                    ans=min(ans,(i-j+1))
                t_sum-=nums[j]
                j+=1
            i+=1
            
        if ans==len(nums)+1:
            return 0
        return ans
