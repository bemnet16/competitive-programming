class Solution(object):
    def totalMoney(self, n):
        mod = n // 7
        tot = 0
        t = 0
        for i in range(mod):
            t += 1
            for j in range(i + 1,i + 8):
                tot = tot + j
            
        
        re = n - (mod * 7) + 1
        for k in range(t + 1, t + re):
            tot = tot + k
        
        
        return tot