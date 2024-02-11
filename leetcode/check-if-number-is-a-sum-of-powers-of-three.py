class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        powers_three = []
        #save power of 3 from 16 - 0 components
        for i in range(16, -1, -1):
            powers_three.append(3 ** i)
            
        answer = [0] * 17
        for i,value in enumerate(powers_three):
            if n >= value:
                answer[i] = value
                n -= value
        
        return n == 0
        
        
        