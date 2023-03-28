class Solution(object):
    def topKFrequent(self, nums, k):
        v=[]
        d={}
        m=[]
        for i in nums:
            if i not in v:
                v.append(i)
                d[i] = nums.count(i)
        l = list(d.values())
        l.sort()
        l = l[::-1]
        for j in d:
            for i in range(k):
                if d[j] == l[i]:
                    m.append(j)
                    break
        return m
                
            
