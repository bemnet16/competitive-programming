class Solution(object):
    def topKFrequent(self, nums, k):
        # d={}
        # for i in nums:
        #     if i not in d:
        #         d[i]=0
        #     d[i]+=1
        # d=sorted(d.items(), key=lambda x:x[1])
        # return [d[i][0]  for i in range(len(d)-k,len(d))]
        
        d={}
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        
        new_sorted = sorted(d.items(), key=lambda k:k[1])
        
        res=[]
        for i in range(k):
            res.append(new_sorted[len(new_sorted)-k+i][0])
        
        return res