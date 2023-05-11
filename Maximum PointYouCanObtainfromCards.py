class Solution(object):
    def maxScore(self, cardPoints, k):
        a=cardPoints[:k]
        ans=sum(a)
        res=ans
        for i in range(k):
            ans=ans-a[k-1-i]+cardPoints[-1-i]
            res=max(ans,res)
        return res
            
