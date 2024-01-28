class Solution(object):
    def arrayRankTransform(self, arr):
        d = dict()
        temp = arr[:]
        temp.sort()
        
        idx = 1
        for n in temp:
            if not n in d:
                d[n] = idx
                idx += 1
        
        for i,v in enumerate(arr):
            arr[i] = d[v]
            
        return arr
        