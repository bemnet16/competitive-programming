class Solution(object):
    def carPooling(self, trips, capacity):
        res = [0] * 1002
        lg = 0
        for p,f,t in trips:
            res[f] += p
            res[t] -= p
            lg = max(lg,t)
            
        for i in range(1,lg):
            res[i] += res[i - 1]
        
        for p in res:
            if p > capacity:
                return False
        
        return True
        
        