from collections import OrderedDict

class Solution(object):
    def firstUniqChar(self, s):
        d = OrderedDict()
        
        for idx,val in enumerate(s):
            if val in d:
                d[val][0] += 1
            else:
                d[val] = [1,idx]
        
        for count,idx in d.values():
            if count == 1:
                return idx
            
        return -1