class Solution(object):
    def checkIfExist(self, arr):
        d = dict()
        
        for i,v in enumerate(arr):
            if v * 2 in d or (v / 2 in d and v %2 == 0):
                return True
            d[v] = i
        
        return False
    