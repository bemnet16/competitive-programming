class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        
        
        def backtrack(i, additives):
            
            if i >= len(num):
                
                if len(additives) <= 2:
                    return False
                
                for j in range(len(additives) - 2):
                    if additives[j] + additives[j + 1] != additives[j + 2]:
                        return False
                return True
            
            # optimize / check every additives if they met the condition
            if len(additives) >= 3:
                if additives[-3] + additives[-2] != additives[-1]:
                    return False
            
            
            for j in range(i, len(num)):
                
                # check leading zeros
                if len(str(int(num[i: j + 1]))) != (j + 1 - i):
                    continue
                    
                additives.append(int(num[i: j + 1]))
                if backtrack(j + 1, additives):
                    return True
                
                additives.pop()
            
            return False
            
        
        
        return backtrack(0, [])
                    
        