from collections import OrderedDict

class Solution(object):
    def firstUniqChar(self, s):
        d = OrderedDict()
        for i,v in enumerate(s):
            if v in d:
                d[v][0] += 1
            else:
                d[v] = [1,i]
        
        for c,i in d.values():
            if c == 1:
                return i
            
        return -1