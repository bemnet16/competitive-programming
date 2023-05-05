class Solution(object):
    def topKFrequent(self, nums, k):
        d={}
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
        d=sorted(d.items(), key=lambda x:x[1])
        return [d[i][0]  for i in range(len(d)-1,len(d)-k-1,-1)]
