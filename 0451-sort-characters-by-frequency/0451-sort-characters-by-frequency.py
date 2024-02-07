class Solution(object):
    def frequencySort(self, s):
        d = {}
        for char in s:
            d[char] = d.get(char,0) + 1
        
        temp = list(d.items())
        temp.sort(key=lambda x:x[1], reverse=True)
        
        res = []
        for v,c in temp:
            for i in range(c):
                res.append(v)
        
        return "".join(res)
        