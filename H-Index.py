class Solution(object):
    def hIndex(self, citations):
        
        citations.sort()
        lg = len(citations)
        
        for i, j in enumerate(citations):
            if j >= lg - i:
                return lg-i
            
        return 0
