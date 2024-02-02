class Solution(object):
    def sequentialDigits(self, low, high):
        st, en = len(str(low)), len(str(high)) + 1
        res = []
        
        for i in range(st,en):
            temp = 0
            inc = 0
            for j in range(1,i + 1):
                temp = temp * 10 + j
                inc = inc * 10 + 1
                
            for k in range(10 - len(str(temp))):
                if low <= temp and temp <= high:
                    res.append(temp)
                temp += inc
                if temp > high:
                    break
        
        return res
                
        