class Solution(object):
    def topKFrequent(self, words, k):
        d={}
        for i in words:
            if i not in d:
                d[i]=0
            d[i]+=1
        d=sorted(d.items(),key=lambda x:(-x[1], x[0]),reverse=False)
        return [d[i][0] for i in range(k)]
