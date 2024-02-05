from collections import OrderedDict

class Solution(object):
    def firstUniqChar(self, s):
        d = OrderedDict()
        for c in s:
            d[c] = d.get(c,0) + 1
        
        for k in d:
            if d[k] == 1:
                return s.index(k)
        
        return -1